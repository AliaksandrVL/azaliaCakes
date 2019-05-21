from django.db import models

class ProductSubcategory(models.Model):

    name = models.CharField(verbose_name='Название подкатегории продукта', max_length=64, unique=True)
    id_product_category = models.ForeignKey('productCategories_app.ProductCategory', on_delete=models.CASCADE)

    def __init__(self):

        return self.name