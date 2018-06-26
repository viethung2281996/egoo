from rest_framework import generics
from . import models, serializers
# Create your views here.

class ListNote(generics.ListCreateAPIView):
  queryset = models.Note.objects.all()
  serializer_class = serializers.NoteSerializer

class DetailNote(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Note.objects.all()
  serializer_class = serializers.NoteSerializer
