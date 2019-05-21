from django.db import models

class Product(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    full_name = models.CharField(verbose_name='Полное наименование', max_length=128)
    characteristic = models.CharField(verbose_name='Характеристика', max_length=512, blank=True)
    consist = models.CharField(verbose_name='Состав', max_length=512, blank=True)
    id_product_subcategory = models.ForeignKey('productSubcategories_app.ProductSubcategory', on_delete=models.CASCADE)

    def __init__(self):

        return self.name
