from rest_framework import serializers
from .models import CustomUser, UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('full_name', 'address', 'photo')

class CustomUserSerializer(serializers.ModelSerializer):
    userdetails = UserDetailsSerializer()

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'full_name', 'address', 'photo', 'is_active', 'is_staff', 'userdetails')
