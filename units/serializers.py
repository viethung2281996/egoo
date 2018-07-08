from units.models import Unit, LEVEL_CHOICE
from django.db import models
from categories.models import Category
from notes.models import Note
from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
  category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
  note_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

  def validate(self, data):
    if self.instance is None:
      list_order_in_category = map(lambda x: x.order, data['category'].list_unit.all())
      if data['order'] in list_order_in_category:
        raise serializers.ValidationError("Order of unit must unique in category")
    return data

  class Meta:
    fields = [
      'id',
      'title',
      'order',
      'image',
      'level',
      'category',
      'note_set'
      ]
    model = Unit

