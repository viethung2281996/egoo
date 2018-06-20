from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from conversations.models import Conversation
from . import serializers
#Create your views here.

class ListConversation(generics.ListCreateAPIView):
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer

class DetailConversation(generics.RetrieveUpdateDestroyAPIView):
  queryset = Conversation.objects.all()
  serializer_class = serializers.ConversationSerializer

@csrf_exempt
def conversation_list(request, pk):
  if request.method == 'GET':
    conversations = Conversation.objects.all()
    serializer = serializers.ConversationSerializer(conversations, many=True)
    return JsonResponse(serializer.data, safe=False)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    print(data)
    serializer = serializers.ConversationSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)