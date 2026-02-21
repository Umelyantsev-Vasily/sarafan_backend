from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from .models import Category, Product, ProductImage, Subcategory


class ProductImageSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ("full", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("medium", "crop__400x400"),
            ("large", "crop__800x800"),
        ]
    )

    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "slug",
            "price",
            "description",
            "subcategory",
            "images",
            "created_at",
        ]


class SubcategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ["id", "name", "slug", "image", "category", "products"]


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "image", "subcategories"]
