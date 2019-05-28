from django.db import models

from django.contrib.auth.models import User


class ProductCategory(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=32, unique=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:

        ordering = ['-name', '-created', '-modified']

    def __str__(self):

        return self.name

class ProductSubcategory(models.Model):

    product_category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE,
                                         verbose_name='Категория продукта')
    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:

        ordering = ['-product_category', '-name', '-created', '-modified']

    def __str__(self):

        return self.name

class Product(models.Model):

    product_subcategory = models.ForeignKey('ProductSubcategory', on_delete=models.CASCADE,
                                            verbose_name='Подкатегория продукта')
    product_measure_unit = models.ForeignKey('ProductMeasureUnit', on_delete=models.CASCADE,
                                             verbose_name='Единица измерения')
    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    full_name = models.CharField(verbose_name='Полное наименование', max_length=128)
    characteristic = models.TextField(verbose_name='Характеристика', blank=True)
    consist = models.TextField(verbose_name='Состав', blank=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:

        ordering = ['-product_subcategory', '-name', '-created', '-modified']

    def __str__(self):

        return self.name

class ProductMeasureUnit(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=16, unique=True)
    full_name = models.CharField(verbose_name='Полное наименование', max_length=32, unique=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:

        ordering = ['-name', '-created', '-modified']

    def __str__(self):

        return self.name

class ProductFeedback(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    feedback = models.TextField(verbose_name='Отзыв')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    deleted = models.BooleanField(verbose_name='Удален')

    class Meta:

        ordering = ['-product', '-user', '-created']

    def __str__(self):

        return self.feedback