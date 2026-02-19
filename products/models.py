from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Создает категории товаров
    """
    name = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL- идентификатор')
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)


class Subcategory(models.Model):
    """
    Создание подкатегории товаров
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories',
                                 verbose_name='Родительская категория')
    name = models.CharField(max_length=255, verbose_name='Подкатегория')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL-идентификатор')
    image = models.ImageField(upload_to='subcategories/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f'{self.name}({self.category.name})'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """
    Создаем продукт
    """
    name = models.CharField(max_length=200, verbose_name='Продукт')
    slug = models.SlugField(unique=True, verbose_name='Уникальное название')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE,
                                    verbose_name='Подкатегория товара')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}({self.subcategory.name})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    """
    Загрузка изображения
    """
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name='Продукт')
    image = models.ImageField(upload_to='products/images', verbose_name='Изображение')

    def __str__(self):
        return f'Изображение для({self.product.name})'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
