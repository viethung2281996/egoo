from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from commons.permissions import UserPermission
from commons.views import UserAPIView
from categories.models import Category
from units.models import Unit
from guides.models import Guide
from guides.serializers import GuideSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from egoo_core.cloudinary import CloudinaryUploader
# Create your views here.

class ListGuide(generics.ListCreateAPIView):
  queryset = Guide.objects.all()
  serializer_class = GuideSerializer
  permission_classes = (UserPermission,)

class DetailGuide(generics.RetrieveUpdateDestroyAPIView):
  queryset = Guide.objects.all()
  serializer_class = GuideSerializer
  permission_classes = (UserPermission,)

class GuideOfUnit(UserAPIView):
  def get(self, request, category_id, unit_id):
    try:
      category = Category.objects.get(id=category_id)
      unit = category.list_unit.get(id=unit_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)

    try:
      guide = unit.guide
    except Exception as e:
      return Response({})

    serializer = GuideSerializer(guide)
    return Response(serializer.data)

@parser_classes((MultiPartParser, ))
class GuideUploadImage(UserAPIView):
  def post(self, request, guide_id):
    try:
      guide = Guide.objects.get(id=guide_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    file = request.FILES['image']

    file_name = guide.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="guides/images")
    r = uploader.upload()
    data['image'] = r['secure_url']
    serializer = GuideSerializer(guide, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)

@parser_classes((MultiPartParser, ))
class GuideUploadVideo(UserAPIView):
  def post(self, request, guide_id):
    try:
      guide = Guide.objects.get(id=guide_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    video_url = request.data.get('video_url', None)
    if video_url is None:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)
    data['video'] = video_url
    serializer = GuideSerializer(guide, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)

