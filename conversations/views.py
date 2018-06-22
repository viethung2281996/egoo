from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from conversations.models import Conversation
from django.core.exceptions import ObjectDoesNotExist
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from units.models import Unit
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
    conversations = unit.list_conversation
    serializer = serializers.ConversationSerializer(conversations, many=True)
    return Response(serializer.data)
