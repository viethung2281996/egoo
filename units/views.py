from rest_framework import generics, permissions,mixins
from rest_framework.response import Response
from api.permissons import UserPermission
from api.views import BaseAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from django.core.exceptions import ObjectDoesNotExist
from units.models import Unit
from units.serializers import UnitSerializer
from categories.models import Category
from egoo_core.cloudinary import CloudinaryUploader
# Create your views here.

class ListUnit(generics.ListCreateAPIView):
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer
  permission_classes = (UserPermission,)
  
class DetailUnit(generics.RetrieveUpdateDestroyAPIView):
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer
  permission_classes = (UserPermission,)

class ListUnitInCategory(BaseAPIView):
  def get(self, request, category_id):
    try:
      category = Category.objects.get(id=category_id)

    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    units = category.list_unit.order_by('order')
    serializer=UnitSerializer(units, many=True)
    return Response(serializer.data)

@parser_classes((MultiPartParser, ))
class UnitUploadImage(BaseAPIView):
  def post(self, request, unit_id):
    try:
      unit = Unit.objects.get(id=unit_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    file = request.data['image']
    file_name = unit.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="units/images")
    r = uploader.upload()
    data['image'] = r['secure_url']

    serializer = UnitSerializer(unit, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)