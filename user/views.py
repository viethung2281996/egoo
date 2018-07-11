from django.shortcuts import render
from rest_framework.permissions import AllowAny
# Create your views here.
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import generics


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

class ListUser(generics.ListCreateAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
