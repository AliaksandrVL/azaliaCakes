from django.urls import path
from . import  views

app_name = 'products_app'

urlpatterns=[
    path('', views.product_list, name='list'),
    path('create', views.product_create, name='create'),
    path('<int:pk>/', views.product_object, name='object')
]