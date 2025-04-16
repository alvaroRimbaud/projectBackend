from rest_framework import generics, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios logueados pueden crear órdenes

    def perform_create(self, serializer):
        # Asigna automáticamente el usuario actual como dueño de la orden
        serializer.save(id_user=self.request.user)

class OrderItemCreateView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios logueados pueden añadir ítems

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(id_user=self.request.user)
    
class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(id_user=self.request.user)
