from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from categories.models import Category
from categories.serializers import CategorySerializer
from units.serializers import UnitSerializer
from egoo_core.cloudinary import CloudinaryUploader
# Create your views here.

class ListCategory(generics.ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  def get_queryset(self):
    return Category.objects.order_by('order')

class DetaiCategory(generics.RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

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
    file = request.data['image']
    file_name = category.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="categories/images")
    r = uploader.upload()
    data['image'] = r['secure_url']
    serializer = CategorySerializer(category, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)
