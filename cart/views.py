from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from products.models import Product

from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Пользователь видит только совoю корзину"""
        return Cart.objects.filter(user=self.request.user)

    def get_or_create_cart(self, user):
        cart, created = Cart.objects.get_or_create(user=user)
        return cart

    @action(detail=False, methods=["post"])
    def add_item(self, request):
        """Добавление товара в корзину"""
        cart = self.get_or_create_cart(request.user)
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        product = get_object_or_404(Product, id=product_id)

        # Пытаемся найти существующий item
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={"price": product.price, "quantity": quantity},
        )

        if not created:
            # Если товар уже есть, увеличиваем количество
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["delete"])
    def clear(self, request):
        """Очистка корзины"""
        cart = self.get_or_create_cart(request.user)
        cart.items.all().delete()
        return Response({"status": "корзина очищена"})

    @action(detail=False, methods=["post"])
    def update_quantity(self, request):
        """Изменение количества товара"""
        cart = self.get_or_create_cart(request.user)
        item_id = request.data.get("item_id")
        quantity = int(request.data.get("quantity", 1))

        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)

        if quantity <= 0:
            cart_item.delete()
            return Response({"status": "товар удален"})

        cart_item.quantity = quantity
        cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    @action(detail=False, methods=["delete"])
    def remove_item(self, request):
        """Удаление конкретного товара"""
        cart = self.get_or_create_cart(request.user)
        item_id = request.data.get("item_id")

        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        cart_item.delete()

        return Response({"status": "товар удален из корзины"})
