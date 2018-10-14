from rest_framework import serializers
from categories.models import Category, ActivationCode
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
  name = models.CharField(max_length=100)
  
  class Meta:
    fields = [
      'id',
      'name',
      'order',
      'image',
      'type',
      'base_price'
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