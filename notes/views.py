from rest_framework import generics
from rest_framework.response import Response
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
# Create your views here.

class ListNote(generics.ListCreateAPIView):
  queryset = models.Note.objects.all()
  serializer_class = serializers.NoteSerializer

class DetailNote(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Note.objects.all()
  serializer_class = serializers.NoteSerializer

@parser_classes((MultiPartParser, ))
class UploadAudio(APIView):
  def post(self, request, note_id):
    try:
      note = models.Note.objects.get(id=note_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    audio_file = request.data['audio']
    data['audio'] = audio_file
    serializer = serializers.NoteSerializer(note, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)