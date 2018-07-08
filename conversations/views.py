from rest_framework import generics
from rest_framework.response import Response
from conversations.models import Conversation
from conversations.serializers import ConversationSerializer
from . import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from egoo_core.cloudinary import CloudinaryUploader
from categories.models import Category
#Create your views here.

class ListConversation(generics.ListCreateAPIView):
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer

class DetailConversation(generics.RetrieveUpdateDestroyAPIView):
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer

class ListConversationInUnit(APIView):
  def get(self, request, category_id, unit_id):
    try:
      category = Category.objects.get(id=category_id)
      unit = category.list_unit.get(id=unit_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    conversations = unit.list_conversation.order_by('order')
    serializer=ConversationSerializer(conversations, many=True)
    return Response(serializer.data)

@parser_classes((MultiPartParser, ))
class UploadImage(APIView):
  def post(self, request, conversation_id):
    try:
      conversation = Conversation.objects.get(id=conversation_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    file = request.FILES['image']

    file_name = conversation.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="conversations/images")
    r = uploader.upload()
    data['image'] = r['secure_url']
    serializer = ConversationSerializer(conversation, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)

@parser_classes((MultiPartParser, ))
class ConversationUploadAudio(APIView):
  def post(self, request, conversation_id):
    try:
      conversation = Conversation.objects.get(id=conversation_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    file = request.data['audio']
    file_name = conversation.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="conversations/audios", resource_type="video")
    r = uploader.upload()
    data['audio'] = r['secure_url']
    serializer = ConversationSerializer(conversation, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)
