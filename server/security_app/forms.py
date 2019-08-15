from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    
    username = forms.CharField(label='Логин', required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', required=True,
        max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        
        self.user = self.login()

        if not self.login():
            raise forms.ValidationError('Wrong user or password')

        super(LoginForm, self).clean(*args, **kwargs)

    def login(self):

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        return authenticate(username=username, password=password)

class SigninForm(forms.ModelForm):

    password_confirm = forms.CharField(label='Password confirm', max_length=32, required=True,
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'password': forms.widgets.PasswordInput(attrs={'class': 'form-control'})
        }
    
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password is not confirm')
        
        return self.cleaned_data
        #super(SigninForm, self).clean_password_confirm()
    
    def save(self, commit=True):
        
        password = self.cleaned_data.get('password')
        user = super(SigninForm, self).save(commit=True)

        user.set_password(password)

        if commit:
            user.save()

        return user