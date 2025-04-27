from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'birthdate', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Para no mostrar la password en las respuestas
        }
        
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            birthdate=validated_data.get('birthdate', None),
        )
        user.set_password(validated_data['password']) 
        user.save()
        return user

        # def validate_email(self, value):
        #     if User.objects.filter(email=value).exists():
        #         raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        #     return value

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user

