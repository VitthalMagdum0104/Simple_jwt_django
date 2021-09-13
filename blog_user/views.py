from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.


class Signup(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HandleSignup(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        if len(username) > 10 or not username.isalnum():
            messages.error(
                request, " Username must contain letters,numbers and less than 10 chars.")

        if password1 != password2:
            messages.error(
                request, " Passwords should match.")

        user = User.objects.create_user(username, email, password1)
        token = RefreshToken.for_user(user)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return Response({'username': username, 'Jwt_refresh_token': str(token),
                         'Jwt_access_token': str(token.access_token), })


class Login(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, " Successfully Logged In.")
            return Response({"meassage": " Successfully Logged In."})
        else:
            messages.error(
                request, " Invalid credintials, Please try again.")
            return Response({"meassage": " Invalid Crediantials."})


def user_logout(request):
    logout(request)
    messages.error(request, "Successfully Logout.")
