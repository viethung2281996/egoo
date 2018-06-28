from rest_framework import serializers
from notes.models import Note
from units.models import Unit

class NoteSerializer(serializers.ModelSerializer):
  units = serializers.PrimaryKeyRelatedField(many=True, queryset=Unit.objects.all())
  audio = serializers.FileField(max_length=None, use_url=True, allow_empty_file=True, read_only=True)

  class Meta:
    fields = (
      'id',
      'text',
      'pronounce',
      'audio',
      'units',
      )
    model = Note
