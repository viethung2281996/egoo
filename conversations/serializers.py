from rest_framework import serializers
from units.models import Unit
from conversations.models import Conversation

class ConversationSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())
  
  def validate(self, data):
    list_order_in_unit = map(lambda x: x.order, data['unit'].list_conversation.all())
    if data['order'] in list_order_in_unit:
        raise serializers.ValidationError("Order of conversations must unique in unit")
    return data

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