from rest_framework import viewsets

from .models import Category, Product, Subcategory
from .serializers import (CategorySerializer, ProductSerializer,
                          SubcategorySerializer)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related("images")
    serializer_class = ProductSerializer
