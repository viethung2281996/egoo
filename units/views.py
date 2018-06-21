from rest_framework import generics
from units.models import Unit
from . import serializers
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListUnit(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Unit.objects.all()
  serializer_class = serializers.UnitSerializer

class DetailUnit(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Unit.objects.all()
  serializer_class = serializers.UnitSerializer