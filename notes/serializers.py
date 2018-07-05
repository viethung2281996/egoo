from rest_framework import serializers
from notes.models import Note
from units.models import Unit

class NoteSerializer(serializers.ModelSerializer):
  units = serializers.PrimaryKeyRelatedField(many=True, queryset=Unit.objects.all())

  class Meta:
    fields = (
      'id',
      'text',
      'pronounce',
      'audio',
      'units',
      )
    model = Note
