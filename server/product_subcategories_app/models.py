from django.db import models

class ProductSubcategory(models.Model):

    name = models.CharField(verbose_name='Название подкатегории продукта', max_length=64, unique=True)
    product_category = models.ForeignKey('product_categories_app.ProductCategory', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:

        ordering = ['-name', '-created', '-modified']

    def __init__(self):

        return self.name