from units.models import Unit, LEVEL_CHOICE
from django.db import models
from categories.serializers import CategorySerializer
from categories.models import Category
from rest_framework import serializers

class UnitSerializer(serializers.ModelSerializer):
  category_id = serializers.IntegerField()
  level = serializers.ChoiceField(choices=LEVEL_CHOICE)

  def create(self, validated_data):
    category_id = validated_data.pop('category_id')
    category = Category.objects.get(id=category_id)
    unit = Unit.objects.create(category=category, **validated_data)
    return unit

  class Meta:
    fields = [
      'id',
      'title',
      'order',
      'level',
      'category_id',
      ]
    model = Unit

