from units.models import Unit
from django.db import models
from categories.serializers import CategorySerializer
from categories.models import Category
from rest_framework import serializers

class UnitSerializer(serializers.ModelSerializer):
  category_id = serializers.IntegerField()

  # def create(self, validated_data):
  #   unit = Unit.objects.create(
  #       title = validated_data["title"],
  #       order = validated_data["order"],
  #     )
   
  #   if unit.save():
  #     return unit

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
      'category_id',
      ]
    model = Unit