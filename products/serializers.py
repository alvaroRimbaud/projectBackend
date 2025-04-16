from rest_framework import serializers, generics
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']

    # def create(self, validated_data):
    #     return Product.objects.create(**validated_data)
