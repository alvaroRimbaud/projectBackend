from rest_framework import generics
from .serializers import UserSerializer
from .models import User

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
