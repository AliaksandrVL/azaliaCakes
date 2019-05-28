from django.contrib import admin

from . import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('owner', 'image', 'name', 'description')
    list_filter = ('owner', 'name')
    search_fields = ['owner', 'name']