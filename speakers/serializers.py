from rest_framework import serializers
from units.models import Unit
from django.contrib.auth import get_user_model
from speakers.models import Speaker

class SpeakerSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
  user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

  class Meta:
    fields = (
      'id',
      'user',
      'unit',
      'score',
      )
    model = Speaker