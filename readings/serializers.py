from rest_framework import serializers
from units.models import Unit
from .models import Reading

class ReadingSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())

  class Meta:
    fields = (
      'id',
      'content',
      'unit',
      )
    model = Reading