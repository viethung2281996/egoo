from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import UserSerializer, CustomInformationSerializer, TicketSerializer
from rest_framework import filters, generics, exceptions, status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from .models import CustomInformation
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from egoo_core.cloudinary import CloudinaryUploader
from user.services import UserActiveCode

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

class ListUser(generics.ListCreateAPIView):
  serializer_class = UserSerializer

  def get_queryset(self):
    queryset = get_user_model().objects.all().order_by('-date_joined')
    email = self.request.query_params.get('email', None)
    if email is not None:
      return queryset.filter(email=email)
    return queryset

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer

@parser_classes((MultiPartParser, ))
class UserUploadAvatar(APIView):
  def post(self, request, pk):
    try:
      user = get_user_model().objects.get(id=pk)
      custom_information = user.custominformation
    except CustomInformation.DoesNotExist:
      custom_information = CustomInformation(user=user)
      custom_information.save()
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
      
    data = {}
    file = request.data['image']
    file_name = custom_information.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="user/avatar", resource_type="image")
    r = uploader.upload()
    data['avatar'] = r['secure_url']
    serializer = CustomInformationSerializer(custom_information, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(UserSerializer(user).data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)

class UserActiveCodeView(APIView):
  def post(self, request):
    data = request.data
    code = data['code']
    service = UserActiveCode(request.user.id, code)
    result = service.process()
    if result == False:
      message = service.messages[0]
      response = {
        'message': message
      }
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
      return Response(status=status.HTTP_200_OK)

class AdminActiveCodeView(APIView):
  def post(self, request, pk):
    data = request.data
    code = data['code']
    service = UserActiveCode(pk, code)
    result = service.process()
    if result == False:
      message = service.messages[0]
      response = {
        'message': message
      }
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
      return Response(status=status.HTTP_200_OK)

class UserTicketsView(APIView):
  def get(self, request, pk):
    try:
      user = get_user_model().objects.get(id=pk)
      tickets = user.ticket_set.all()
      serializer = TicketSerializer(tickets, many=True)
      return Response(serializer.data)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)