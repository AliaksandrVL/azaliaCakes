from django.db import models

class ProductCategory(models.Model):

    name = models.CharField(verbose_name='Название категории продукта', max_length=64, unique=True)

    def __init__(self):

        return self.name