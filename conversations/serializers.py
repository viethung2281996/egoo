from rest_framework import serializers
from units.models import Unit
from conversations.models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())
  image = serializers.ImageField(max_length=None, use_url=True, allow_empty_file=True, read_only=True)
  audio = serializers.FileField(max_length=None, use_url=True, allow_empty_file=True, read_only=True)
  class Meta:
    fields = (
      'id',
      'context',
      'image',
      'audio',
      'order',
      'unit',
      'is_robot',
      'recommend'
      )
    model = Conversation