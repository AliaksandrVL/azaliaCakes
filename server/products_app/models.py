from django.db import models

class Product(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    full_name = models.CharField(verbose_name='Полное наименование', max_length=128)
    characteristic = models.CharField(verbose_name='Характеристика', max_length=512, blank=True)
    consist = models.CharField(verbose_name='Состав', max_length=512, blank=True)
    product_subcategory = models.ForeignKey('product_subcategories_app.ProductSubcategory', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        
        ordering = ['-name', '-created', '-modified']

    def __init__(self):

        return self.name
