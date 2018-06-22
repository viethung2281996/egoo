from rest_framework import generics, permissions
from categories.models import Category
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer

class DetaiCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer
