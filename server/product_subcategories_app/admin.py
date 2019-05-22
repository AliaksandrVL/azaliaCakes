from django.contrib import admin

from . import models

@admin.register(models.ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):

    list_display = ('product_category', 'name', 'created', 'modified')
    list_filter = ('product_category', 'name')
    search_fields = ['product_category', 'name']
