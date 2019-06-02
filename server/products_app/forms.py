from django import forms
from . import models


class ProductForm(forms.ModelForm):
    
    class Meta:

        model = models.Product
        fields = ['product_subcategory', 'product_measure_unit', 'name', 'full_name', 'characteristic', 'consist']
        widgets = {
            'product_subcategory': forms.Select(attrs={'class': 'form-control'}),
            'product_measure_unit': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'characteristic': forms.Textarea(attrs={'class': 'form-control'}),
            'consist': forms.Textarea(attrs={'class': 'form-control'})
        }