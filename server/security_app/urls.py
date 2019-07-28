from django.urls import path

from . import views


app_name = 'security_app'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
]
