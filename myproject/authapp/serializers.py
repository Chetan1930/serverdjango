from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data

class TodoSerializer(serializers.ModelSerializer):
    
    permission_class= [IsAuthenticated]
    
    class Meta:
        model= Todo
        fields ='__all__'
        read_only_fields = ['user','created_at']
    