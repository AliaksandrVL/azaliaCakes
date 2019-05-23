from django.shortcuts import render

from django.http import HttpResponse
from . import models

def index(request):

    query = models.Product.objects.all()

    return render(request, 'products_app/index.html', {'quey': query})