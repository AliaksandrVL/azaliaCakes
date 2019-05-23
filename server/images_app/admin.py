from django.contrib import admin

from . import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('product', 'image', 'name', 'description')
    list_filter = ('product', 'name')
    search_fields = ['product', 'name']