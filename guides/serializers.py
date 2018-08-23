from rest_framework import serializers
from units.models import Unit
from guides.models import Guide

class GuideSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())

  class Meta:
    fields = (
      'id',
      'content',
      'video',
      'image',
      'unit'
      )
    model = Guide