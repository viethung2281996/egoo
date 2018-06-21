from rest_framework import serializers
# from units.serializers import UnitSerializer
from categories.models import Category
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
  name = models.CharField(max_length=100)
  class Meta:
    fields = [
      'id',
      'name'
      ]
    model = Category

  # def create(self, validated_data):
  #   units_data = validated_data.pop('list_unit')
  #   category = Category.objects.create(**validated_data)
  #   for unit_data in unit_data:
  #     Unit.objects.create(category=category, **unit_data)
  #   return category

  # def update(self, instance, validated_data):
  #   units_data = validated_data.pop('list_unit')
  #   units = (instance.list_unit).all()
  #   units = list(units)
  #   instance.name = validated_data.get('name', instance.name)
  #   instance.save()

  #   for unit_data in units_data:
  #     unit = units.pop(0)
  #     unit.title = unit_data.get('title', unit.title)
  #     unit.order = unit_data.get('order', unit.order)
  #     unit.save()

  #   return instance
