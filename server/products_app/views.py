from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    return render(request, 'products_app/index.html', {'content': 'Hello world!'})