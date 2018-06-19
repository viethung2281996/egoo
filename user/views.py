from django.shortcuts import render
from rest_framework.permissions import AllowAny
# Create your views here.
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer