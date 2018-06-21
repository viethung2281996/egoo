from rest_framework import generics, permissions
from categories.models import Category
from . import serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.

<<<<<<< HEAD
class ListCategory(generics.ListCreateAPIView): 
=======
class ListCategory(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
>>>>>>> 234a47ffa7b046e38f9f8b70994f9db76ba0be4a
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer

class DetaiCategory(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Category.objects.all()
  serializer_class = serializers.CategorySerializer