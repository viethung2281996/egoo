from rest_framework import serializers
from units.serializers import UnitSerializer
from conversations.models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
  unit = UnitSerializer(read_only=True)
  class Meta:
    fields = (
      'id',
      'context',
      'image',
      'audio',
      'order',
      'unit',
      )
    model = Conversation