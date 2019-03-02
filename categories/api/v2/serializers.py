from rest_framework import serializers
from categories.models import Category, ActivationCode
from units.models import Unit
from django.db import models
from units.serializers import UnitSerializer

class CategorySerializer(serializers.ModelSerializer):
  name = models.CharField(max_length=100)
  list_unit = UnitSerializer(many=True, read_only=True)

  class Meta:
    fields = [
      'id',
      'name',
      'order',
      'image',
      'type',
      'base_price',
      'list_unit'
      ]
    model = Category

class ActivationCodeSerializer(serializers.ModelSerializer):
  category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
  class Meta:
    fields = [
      'id',
      'code',
      'status',
      'type',
      'time',
      'category'
    ]
    model = ActivationCode