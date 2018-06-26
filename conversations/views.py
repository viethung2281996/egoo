from rest_framework import generics
from conversations.models import Conversation
from . import serializers
#Create your views here.

class ListConversation(generics.ListCreateAPIView):
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer

class DetailConversation(generics.RetrieveUpdateDestroyAPIView):
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer
