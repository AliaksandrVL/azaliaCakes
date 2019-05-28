from django.contrib import admin

from . import models


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'created', 'modified')
    list_filter = ('name',)
    search_fields = ['name',]

@admin.register(models.ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):

    list_display = ('product_category', 'name', 'created', 'modified')
    list_filter = ('product_category', 'name')
    search_fields = ['product_category', 'name']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('product_subcategory', 'name', 'full_name', 'product_measure_unit', 'created', 'modified')
    list_filter = ('product_subcategory', 'name', 'full_name', 'product_measure_unit')
    search_fields = ['product_subcategory', 'name', 'full_name', 'product_measure_unit']

@admin.register(models.ProductMeasureUnit)
class ProductMeasureUnitAdmin(admin.ModelAdmin):

    list_display = ('name', 'full_name', 'created', 'modified')
    list_filter = ('name', 'full_name')
    search_fields = ['name', 'full_name']

@admin.register(models.ProductFeedback)
class ProductFeedbacksAdmin(admin.ModelAdmin):

    list_display = ('product', 'user', 'created', 'deleted')
    list_filter = ('product', 'user', 'created', 'deleted')
    search_fields = ['product', 'user']