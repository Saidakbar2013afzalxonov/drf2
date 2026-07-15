from django.urls import path, include
from .views import ProductView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("products/", ProductView.as_view({'get':'list'})),
    path("products/create/", ProductView.as_view({'post':'create'})),
    path("products/update/<int:pk>/", ProductView.as_view({'put':'update', 'patch':'partial_update'})),
    path("products/delete/<int:pk>/", ProductView.as_view({'delete':'destroy'})),
]