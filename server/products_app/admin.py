from django.contrib import admin

from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_subcategory', 'name', 'full_name', 'created', 'modified')
    list_filter = ('product_subcategory', 'name', 'full_name')
    search_fields = ['product_subcategory', 'name', 'full_name']