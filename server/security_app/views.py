from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login

from . import forms
from . import mixins


class LoginView(mixins.AnonRequired, FormView):

    form_class = forms.LoginForm
    success_url = reverse_lazy('products_app:list')
    main_url = reverse_lazy('products_app:list')
    template_name = 'security/login.htm'

    def post(self, request):
        
        form = self.form_class(request.POST)

        if form.is_valid():
            login(request, form.user)
            
            return redirect(self.success_url)
        
        return render(request, self.template_name, {'form': form})

class SigninView(mixins.AnonRequired, FormView):

    form_class = forms.SigninForm
    success_url = reverse_lazy('products_app:list')
    main_url = reverse_lazy('products_app:list')
    template_name = 'security/signin.htm'
    
    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            
            login(request, user)

            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})