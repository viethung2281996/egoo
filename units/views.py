from rest_framework import generics, permissions,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from units.models import Unit
from . import serializers
from rest_framework.permissions import IsAuthenticated
from categories.models import Category
# Create your views here.

class ListUnit(generics.ListCreateAPIView):
  authentication_classes = (SessionAuthentication, BasicAuthentication)
  permission_classes = (IsAuthenticated,)
  queryset = Unit.objects.all()
  serializer_class = serializers.UnitSerializer

class DetailUnit(generics.RetrieveUpdateDestroyAPIView):
  pauthentication_classes = (SessionAuthentication, BasicAuthentication)
  permission_classes = (IsAuthenticated,)
  queryset = Unit.objects.all()
  serializer_class = serializers.UnitSerializer

class ListUnitInCategory(APIView):
  authentication_classes = (SessionAuthentication, BasicAuthentication)
  permission_classes = (IsAuthenticated,)
  def get(self, request, category_id):
    try:
      category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    units = category.list_unit
    serializer = serializers.UnitSerializer(units, many=True)
    return Response(serializer.data)