from django.shortcuts import render
from rest_framework import generics, status
from commons.permissions import UserPermission
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from .models import Exsercise, ListenAndReadExsercise, ChoseAnswerExsercise, RewriteSentenceExsercise, TranslateSentenceExsercise
from .helpers import ListenAndReadExserciseHelper, ChoseAnswerExserciseHelper, TranslateSentenceExserciseHelper, RewriteSentenceExserciseHelper
from .serializers import ExserciseSerializer, ListenAndReadExserciseSerializer, ChoseAnswerExserciseSerializer, RewriteSentenceExserciseSerializer, TranslateSentenceExserciseSerializer
from commons.views import UserAPIView, AdminAPIView
from categories.models import Category
# Create your views here.
class ListExsercise(generics.ListCreateAPIView):
  queryset = Exsercise.objects.all()
  permission_classes = (UserPermission,)

class DetailExsercise(generics.RetrieveUpdateDestroyAPIView):
  queryset = Exsercise.objects.all()
  permission_classes = (UserPermission,)

class ListListenAndReadExsercise(ListExsercise):
  queryset = ListenAndReadExsercise.objects.all()
  serializer_class = ListenAndReadExserciseSerializer

class DetailListenAndReadExsercise(DetailExsercise):
  queryset = ListenAndReadExsercise.objects.all()
  serializer_class = ListenAndReadExserciseSerializer

@parser_classes((MultiPartParser, ))
class ListenAndReadExserciseUploadImage(AdminAPIView):
  def post(self, request, exsercise_id):
    exsercise = ListenAndReadExserciseHelper.get_object(exsercise_id)
    file = request.data['image']

    if exsercise is None or file is None:
      response = {"message": "Invalid input data"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    result_url = ListenAndReadExserciseHelper.upload(exsercise, file, folder="exsercises/images", resource_type="image")

    data = {}
    data['image'] = result_url

    data = ListenAndReadExserciseHelper.update_data(exsercise, data=data)
    if data is not None:
      return Response(data, status=status.HTTP_200_OK)
    else:
      response = {"message": "Upload file failed"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@parser_classes((MultiPartParser, ))
class ListenAndReadExserciseUploadAudio(AdminAPIView):
  def post(self, request, exsercise_id):
    exsercise = ListenAndReadExserciseHelper.get_object(exsercise_id)
    file = request.data['audio']

    if exsercise is None or file is None:
      response = {"message": "Invalid input data"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    result_url = ListenAndReadExserciseHelper.upload(exsercise, file, folder="exsercises/video", resource_type="video")

    data = {}
    data['audio'] = result_url

    data = ListenAndReadExserciseHelper.update_data(exsercise, data=data)
    if data is not None:
      return Response(data, status=status.HTTP_200_OK)
    else:
      response = {"message": "Upload file failed"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ListChoseAnswerExsercise(ListExsercise):
  queryset = ChoseAnswerExsercise.objects.all()
  serializer_class = ChoseAnswerExserciseSerializer

class DetailChoseAnswerExsercise(DetailExsercise):
  queryset = ChoseAnswerExsercise.objects.all()
  serializer_class = ChoseAnswerExserciseSerializer

@parser_classes((MultiPartParser, ))
class ChoseAnswerExserciseUploadImage(AdminAPIView):
  def post(self, request, exsercise_id):
    exsercise = ChoseAnswerExserciseHelper.get_object(exsercise_id)
    file = request.data['image']

    if exsercise is None or file is None:
      response = {"message": "Invalid input data"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    result_url = ChoseAnswerExserciseHelper.upload(exsercise, file, folder="exsercises/images", resource_type="image")

    data = {}
    data['image'] = result_url

    data = ChoseAnswerExserciseHelper.update_data(exsercise, data=data)
    if data is not None:
      return Response(data, status=status.HTTP_200_OK)
    else:
      response = {"message": "Upload file failed"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@parser_classes((MultiPartParser, ))
class ChoseAnswerExserciseUploadAudio(AdminAPIView):
  def post(self, request, exsercise_id):
    exsercise = ChoseAnswerExserciseHelper.get_object(exsercise_id)
    file = request.data['audio']

    if exsercise is None or file is None:
      response = {"message": "Invalid input data"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    result_url = ChoseAnswerExserciseHelper.upload(exsercise, file, folder="exsercises/video", resource_type="video")

    data = {}
    data['audio'] = result_url

    data = ChoseAnswerExserciseHelper.update_data(exsercise, data=data)
    if data is not None:
      return Response(data, status=status.HTTP_200_OK)
    else:
      response = {"message": "Upload file failed"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ListRewriteSentenceExsercise(ListExsercise):
  queryset = RewriteSentenceExsercise.objects.all()
  serializer_class = RewriteSentenceExserciseSerializer

class DetailRewriteSentenceExsercise(DetailExsercise):
  queryset = RewriteSentenceExsercise.objects.all()
  serializer_class = RewriteSentenceExserciseSerializer

@parser_classes((MultiPartParser, ))
class RewriteSentenceExserciseUploadAudio(AdminAPIView):
  def post(self, request, exsercise_id):
    exsercise = RewriteSentenceExserciseHelper.get_object(exsercise_id)
    file = request.data['audio']

    if exsercise is None or file is None:
      response = {"message": "Invalid input data"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    result_url = RewriteSentenceExserciseHelper.upload(exsercise, file, folder="exsercises/video", resource_type="video")

    data = {}
    data['audio'] = result_url

    data = RewriteSentenceExserciseHelper.update_data(exsercise, data=data)
    if data is not None:
      return Response(data, status=status.HTTP_200_OK)
    else:
      response = {"message": "Upload file failed"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class ListTranslateSentenceExsercise(ListExsercise):
  queryset = TranslateSentenceExsercise.objects.all()
  serializer_class = TranslateSentenceExserciseSerializer

class DetailTranslateSentenceExsercise(DetailExsercise):
  queryset = TranslateSentenceExsercise.objects.all()
  serializer_class = TranslateSentenceExserciseSerializer

@parser_classes((MultiPartParser, ))
class TranslateSentenceExserciseUploadImage(AdminAPIView):
  def post(self, request, exsercise_id):
    try:
      exsercise = TranslateSentenceExserciseHelper.get_object(exsercise_id)
      file = request.data['image']

      if exsercise is None or file is None:
        response = {"message": "Invalid input data"}
        return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

      result_url = TranslateSentenceExserciseHelper.upload(exsercise, file, folder="exsercises/images", resource_type="image")

      data = {}
      data['image'] = result_url

      data = TranslateSentenceExserciseHelper.update_data(exsercise, data=data)
      if data is not None:
        return Response(data, status=status.HTTP_200_OK)
      else:
        response = {"message": "Upload file failed"}
        return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
      raise e

class ExsercisesOfUnit(UserAPIView):
  def get(self, request, category_id, unit_id):
    try:
      category = Category.objects.get(id=category_id)
      unit = category.list_unit.get(id=unit_id)
    except ObjectDoesNotExist:
      response = {"message": "Object doesn't exist"}
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
      
    try:
      exsercises = unit.exsercise_set.all().order_by('order')
    except Exception as e:
      return Response({})
    serializer = ExserciseSerializer(exsercises, many=True)
    return Response(serializer.data)
