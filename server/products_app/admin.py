from django.contrib import admin

from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'full_name', 'created', 'modified')
    list_filter = ('name', 'full_name')
    search_fields = ['name', 'full_name']