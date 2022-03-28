from django.contrib import auth
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from .serializers import LoginSerializer, UserRegister
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

import jwt
# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = UserRegister

    def post(self, request):
        serializer = UserRegister(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
        
    def get(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
    
        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")
            serializer = UserRegister(user)
            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
