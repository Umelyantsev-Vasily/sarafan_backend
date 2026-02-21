from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product


class Cart(models.Model):
    """Корзина товаров"""

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="cart",
        verbose_name="Корзина",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Корзина пользователя {self.user}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    """Товары корзины"""

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_items"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    class Meta:
        unique_together = ["cart", "product"]
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
