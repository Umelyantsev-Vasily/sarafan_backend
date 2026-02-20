from rest_framework import serializers
from .models import ProductImage, Product, Subcategory, Category


class ProductImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProductImage
            fields = ['id', 'image']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields =['id', 'name', 'slug', 'price', 'description', 'subcategory', 'images', 'created_at']


class SubcategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'slug', 'image', 'category', 'products']


class CategorySerializer(serializers.ModelSerializer):

    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name' , 'slug', 'image', 'subcategories' ]


