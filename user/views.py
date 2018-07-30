from django.shortcuts import render
from rest_framework.permissions import AllowAny
# Create your views here.
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

class ListUser(generics.ListCreateAPIView):
  serializer_class = UserSerializer

  def get_queryset(self):
    queryset = get_user_model().objects.all().order_by('-date_joined')
    email = self.request.query_params.get('email', None)
    if email is not None:
      return queryset.filter(email=email)
    return queryset

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
