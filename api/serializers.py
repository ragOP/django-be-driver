# api_app/serializers.py
from rest_framework import serializers
from .models import CustomUser, DriverUser

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

class DriverCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = ['email']

class DriverLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email']

class DriverUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = ['id', 'email']

class DriverUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = ['email']

class CustomUserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = []

class DriverUserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverUser
        fields = []
