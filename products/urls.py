from django.urls import path
from .views import ProductCreateView, ProductListView

urlpatterns = [
    path('crear/', ProductCreateView.as_view(), name='product-create'),  # Solo admin
    path('listar/', ProductListView.as_view(), name='product-list'),     # Público
]
