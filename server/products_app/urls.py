from django.urls import path

from . import  views


app_name = 'products_app'

urlpatterns=[
    path('', views.ProductListView.as_view(), name='list'),
    path('create', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete')
]