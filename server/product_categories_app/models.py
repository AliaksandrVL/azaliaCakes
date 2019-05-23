from django.db import models

class ProductCategory(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    class Meta:

        ordering = ['-name', '-created', '-modified']

    def __str__(self):

        return self.name