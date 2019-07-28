from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    
    username = forms.CharField(label='Логин', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pasword = forms.CharField(label='Пароль', required=True, max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):

        self.user = self.login()

        if not self.login():
            raise forms.ValidationError('Wrong user or password')

        super(LoginForm, self).clean(**args, **kwargs)

    def login(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        return authenticate(username=username, password=password)