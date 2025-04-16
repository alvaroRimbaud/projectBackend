from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Product
from .serializers import ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]  # Solo accesible para admins

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
