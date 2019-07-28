from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import authenticate, login

from . import forms


class LoginView(FormView):

    form_class = forms.LoginForm
    success_url = reverse_lazy('products_app:list')
    template_name = 'security/login.htm'

    def post(self, request):
        
        form = self.form_class(request.POST)

        if form.is_valid():
            login(request, form.user)
            
            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})