from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from categories.models import Category
from categories.serializers import CategorySerializer
from units.serializers import UnitSerializer
from egoo_core.utils import add_url_serializer
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class DetaiCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ListUnitInCategory(APIView):
  def get(self, request, category_id):
    try:
      category = Category.objects.get(id=category_id)

    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    units = category.list_unit
    serializer = add_url_serializer(request, serializer=UnitSerializer(units, many=True))
    return Response(serializer.data)

@parser_classes((MultiPartParser, ))
class CategoryUploadImage(APIView):
  def post(self, request, category_id):
    try:
      category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    image_file = request.data['image']
    data['image'] = image_file
    serializer = CategorySerializer(category, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)
