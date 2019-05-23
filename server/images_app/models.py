from django.db import models

class Image(models.Model):

    product = models.ForeignKey('products_app.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    image = models.ImageField(verbose_name='Изображение')
    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:

        ordering = ['-product', '-name', '-created', '-modified']

    def __str__(self):

        return self.name