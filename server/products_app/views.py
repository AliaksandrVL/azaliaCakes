from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, ListView, DetailView, DeleteView, UpdateView

from . import models
from . import forms


class ProductListView(ListView):
    
    queryset = get_list_or_404(models.Product)
    context_object_name = 'query'
    template_name = 'products_app/index.htm'

class ProductDetailView(DetailView):
    
    model = models.Product
    context_object_name = 'instance'
    template_name = 'products_app/detail.htm'

class ProductCreateView(CreateView):

    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('products_app:list')
    template_name = 'products_app/edit.htm'

class ProductUpdateView(UpdateView):

    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('products_app:detail')
    template_name = 'products_app/edit.htm'

class ProductDeleteView(DeleteView):

    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('products_app:list')
    template_name = 'products_app/delete.htm'