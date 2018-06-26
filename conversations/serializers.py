from rest_framework import serializers
from units.models import Unit
from conversations.models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())
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