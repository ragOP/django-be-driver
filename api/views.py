# api_app/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import CustomUser, DriverUser
from .serializers import DriverCreateSerializer, DriverLoginSerializer, UserCreateSerializer, UserLoginSerializer
import random

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate OTP (6-digit random number)
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

        # Save the user without password
        user = serializer.save()

        # Here, you would send the OTP to the user's email or mobile
        # For simplicity, we'll just include the OTP in the response
        return Response({'email': user.email, 'otp': otp}, status=status.HTTP_201_CREATED)
    
class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']

        # Check if the user exists with the provided email
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"detail": "Invalid email or OTP"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the OTP (In a real-world scenario, this would be sent via email/SMS and verified securely)
        saved_otp = "123456"  # Replace this with the OTP saved during signup

        if otp == saved_otp:
            return Response({"message": "Successful hogya bhai"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid email or OTP"}, status=status.HTTP_400_BAD_REQUEST)
        


class DriveCreateView(generics.CreateAPIView):
    queryset = DriverUser.objects.all()
    serializer_class = DriverCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate OTP (6-digit random number)
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

        # Save the user without password
        user = serializer.save()

        # Here, you would send the OTP to the user's email or mobile
        # For simplicity, we'll just include the OTP in the response
        return Response({'email': user.email, 'otp': otp}, status=status.HTTP_201_CREATED)
    
class DriveLoginView(generics.CreateAPIView):
    serializer_class = DriverLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']

        # Check if the user exists with the provided email
        try:
            user = DriverUser.objects.get(email=email)
        except DriverUser.DoesNotExist:
            return Response({"detail": "Invalid email or OTP"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate the OTP (In a real-world scenario, this would be sent via email/SMS and verified securely)
        saved_otp = "123456"  # Replace this with the OTP saved during signup

        if otp == saved_otp:
            return Response({"message": "Successful hogya bhai"}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid email or OTP"}, status=status.HTTP_400_BAD_REQUEST)
