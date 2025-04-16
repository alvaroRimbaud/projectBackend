from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

        def validate_email(self, value):
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("Este correo electrónico ya está registrado.")
            return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

