from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from conversations.models import Conversation
from . import serializers
from rest_framework.permissions import IsAuthenticated
#Create your views here.

class ListConversation(generics.ListCreateAPIView):
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer

class DetailConversation(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer