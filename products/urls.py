from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('crear/', ProductCreateView.as_view(), name='product-create'),  # Solo admin
    path('listar/', ProductListView.as_view(), name='product-list'),     # Público
    path('actualizar/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('eliminar/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
]
