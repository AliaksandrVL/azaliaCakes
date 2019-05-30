from django.shortcuts import render, get_list_or_404, get_object_or_404

from django.http import HttpResponse
from . import models

def product_list(request):

    query = get_list_or_404(models.Product)

    return render(request, 'products_app/index.htm', {'query': query})

def product_object(request, pk):

    instance = get_object_or_404(models.Product, id=pk)

    return render(request, 'products_app/object.htm', {'instance': instance})