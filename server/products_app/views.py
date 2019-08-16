from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from . import models
from . import forms


class ProductListView(ListView):
    
    queryset = get_list_or_404(models.Product)
    context_object_name = 'query'
    template_name = 'products_app/index.htm'
    paginate_by = 1

class ProductDetailView(DetailView):
    
    model = models.Product
    context_object_name = 'instance'
    template_name = 'products_app/detail.htm'

class ProductCreateView(LoginRequiredMixin, CreateView):

    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('products_app:list')
    login_url = reverse_lazy('security_app:login')
    template_name = 'products_app/edit.htm'

class ProductUpdateView(LoginRequiredMixin, UpdateView):

    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('products_app:detail')
    login_url = reverse_lazy('security_app:login')
    template_name = 'products_app/edit.htm'

class ProductDeleteView(LoginRequiredMixin, DeleteView):

    model = models.Product
    form_class = forms.ProductForm
    success_url = reverse_lazy('products_app:list')
    login_url = reverse_lazy('security_app:login')
    template_name = 'products_app/delete.htm'