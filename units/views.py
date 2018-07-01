from rest_framework import generics, permissions,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from django.core.exceptions import ObjectDoesNotExist
from units.models import Unit
from units.serializers import UnitSerializer
from conversations.serializers import ConversationSerializer
from notes.serializers import NoteSerializer
from categories.models import Category
from egoo_core.utils import add_url_serializer, add_url_serializer_conversations, add_url_serializer_notes
# Create your views here.

class ListUnit(generics.ListCreateAPIView):
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer

class DetailUnit(generics.RetrieveUpdateDestroyAPIView):
  queryset = Unit.objects.all()
  serializer_class = UnitSerializer

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
    serializer = add_url_serializer_conversations(request, serializer=ConversationSerializer(conversations, many=True))
    return Response(serializer.data)

class ListNoteInUnit(APIView):
  def get(self, request, category_id, unit_id):
    try:
      category = Category.objects.get(id=category_id)
      unit = category.list_unit.get(id=unit_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    notes = unit.note_set.all()
    serializer = add_url_serializer_notes(request, serializer=NoteSerializer(notes, many=True))
    return Response(serializer.data)

@parser_classes((MultiPartParser, ))
class UnitUploadImage(APIView):
  def post(self, request, unit_id):
    try:
      unit = Unit.objects.get(id=unit_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    image_file = request.data['image']
    data['image'] = image_file
    serializer = UnitSerializer(unit, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)