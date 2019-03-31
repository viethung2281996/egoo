from rest_framework import generics
from rest_framework.response import Response
from commons.permissions import UserPermission
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
from django.core.exceptions import ObjectDoesNotExist

from commons.views import UserAPIView
from egoo_core.cloudinary import CloudinaryUploader
from notes.serializers import NoteSerializer
from notes.models import Note
from categories.models import Category
# Create your views here.

class ListNote(generics.ListCreateAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = (UserPermission,)

class DetailNote(generics.RetrieveUpdateDestroyAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = (UserPermission,)

class ListNoteInUnit(UserAPIView):
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
    serializer=NoteSerializer(notes, many=True)
    return Response(serializer.data)

@parser_classes((MultiPartParser, ))
class UploadAudio(UserAPIView):
  def post(self, request, note_id):
    try:
      note = Note.objects.get(id=note_id)
    except ObjectDoesNotExist:
      response = {
         "message": "Object doesn't exist"
      }
      return Response(response)
    data = {}
    file = request.data['audio']
    file_name = note.init_file_name(file)
    if file_name == "":
      response = {
         "message": "file name error"
      }
      return Response(response)
    uploader = CloudinaryUploader(file=file,public_id=file_name,folder="notes/audios", resource_type="video")
    r = uploader.upload()
    data['audio'] = r['secure_url']
    serializer = NoteSerializer(note, data=data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      response = {
         "message": "Upload file failed"
      }
      return Response(response)