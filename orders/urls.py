from django.urls import path
from .views import (
    OrderCreateView, OrderListView, OrderDetailView,
    OrderItemCreateView
)

urlpatterns = [
    path('crear/', OrderCreateView.as_view(), name='order-create'),
    path('listar/', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

    # Nuevo endpoint para agregar ítems a una orden
    path('agregar-item/', OrderItemCreateView.as_view(), name='orderitem-create'),
]
