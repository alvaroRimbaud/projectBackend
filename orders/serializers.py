from rest_framework import serializers
from .models import Order, OrderItem
# from products.models import Product
from products.serializers import ProductSerializer

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    id_product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'id_product', 'quantity', 'unitary_price', 'total_price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)  # Esto viene del related_name='items'

    class Meta:
        model = Order
        fields = ['id', 'id_user', 'date_order', 'total_amount', 'items']
