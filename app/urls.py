from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList, name='product-list'),
    path('product/<int:pk>/', views.ProductView, name='product-view'),
    path('product/create/', views.ProductCreate, name='product-create'),
    path('product/update/<int:pk>/', views.ProductUpdate, name='product-update'),
    path('product/delete/<int:pk>/', views.ProductDelete, name='product-delete'),

    path('products-list-create/', views.ProductListCreate, name='product-list-create'),
    path('product-detail/<int:pk>/', views.ProductDetail, name='product-detail'),
]