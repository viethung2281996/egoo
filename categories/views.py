from rest_framework import generics
from categories.models import Category
from . import serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer

class DetaiCategory(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer