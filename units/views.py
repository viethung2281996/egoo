from rest_framework import generics
from units.models import Unit
from . import serializers
# Create your views here.

class ListUnit(generics.ListCreateAPIView):
  queryset = Unit.objects.all()
  serializer_class = serializers.UnitSerializer

class DetailUnit(generics.RetrieveUpdateDestroyAPIView):
  queryset = Unit.objects.all()
  serializer_class = serializers.UnitSerializer