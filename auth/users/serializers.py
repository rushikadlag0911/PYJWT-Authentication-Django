
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserRegister

class UserRegister(serializers.ModelSerializer):
      
    # def encryptPassword(password):
    #     key = Fernet.generate_key()
    #     fernet = Fernet(key)
    #     encpassword = fernet.encrypt(password.encode())
    #     return encpassword

    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    # enc_pass =  pbkdf2_sha256.hash("password")
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email is already in use please try with new Email')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    
    # enc_pass =  pbkdf2_sha256.hash("password")
    class Meta:
        model = User
        fields = ['username','password']