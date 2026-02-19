from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'subcategory', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['subcategory']
    search_fields = ['name', 'description']


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']
    list_filter = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
