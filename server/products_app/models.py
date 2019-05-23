from django.db import models

class Product(models.Model):

    product_subcategory = models.ForeignKey('product_subcategories_app.ProductSubcategory', on_delete=models.CASCADE,
                                            verbose_name='Подкатегория продукта')
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