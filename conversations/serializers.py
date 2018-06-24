from rest_framework import serializers
from units.serializers import UnitSerializer
from units.models import Unit
from conversations.models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
  unit_id = serializers.IntegerField()
  class Meta:
    fields = (
      'id',
      'context',
      'image',
      'audio',
      'order',
      'unit_id'
      )
    model = Conversation

  def create(self, validated_data):
    unit_id = validated_data.pop('unit_id')
    unit = Unit.objects.get(id=unit_id)
    conversation = Conversation.objects.create(unit=unit, **validated_data)
    return conversation