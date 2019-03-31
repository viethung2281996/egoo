from rest_framework import generics, status
from commons.permissions import UserPermission
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import Reading
from .serializers import ReadingSerializer
from commons.views import UserAPIView
from categories.models import Category

# Create your views here.
class ListReading(generics.ListCreateAPIView):
  queryset = Reading.objects.all()
  serializer_class = ReadingSerializer
  permission_classes = (UserPermission,)

class DetailReading(generics.RetrieveUpdateDestroyAPIView):
  queryset = Reading.objects.all()
  serializer_class = ReadingSerializer
  permission_classes = (UserPermission,)

class ReadingOfUnit(UserAPIView):
  def get(self, request, category_id, unit_id):
    try:
      category = Category.objects.get(id=category_id)
      unit = category.list_unit.get(id=unit_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    try:
      reading = unit.reading
    except Exception as e:
      return Response({})

    serializer = ReadingSerializer(reading)
    return Response(serializer.data)