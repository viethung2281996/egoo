from rest_framework import generics, permissions,mixins
from rest_framework.response import Response
from commons.permissions import UserPermission
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from django.core.exceptions import ObjectDoesNotExist
from units.models import Unit

from commons.views import UserAPIView, AdminAPIView
from speakers.models import Speaker
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

class ListUnitInCategory(UserAPIView):
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

    units = self.get_max_score_unit(request, serializer.data)
    return Response(units)

  @staticmethod
  def get_max_score_unit(request, units):
    user_id = request.user.id
    for unit in units:
      score = 0
      speaker_array = Speaker.objects.filter(user=user_id, unit=unit['id'])
      score_array = list(map(lambda x: x.score, speaker_array))
      if len(score_array) > 0:
        score = max(score_array)
      unit['max_score'] = score

    return units

@parser_classes((MultiPartParser, ))
class UnitUploadImage(AdminAPIView):
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