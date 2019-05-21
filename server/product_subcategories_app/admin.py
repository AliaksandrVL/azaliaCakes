from django.contrib import admin

from . import models

@admin.register(models.ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'created', 'modified')
    list_filter = ('name',)
    search_fields = ['name',]
