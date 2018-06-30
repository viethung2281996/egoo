from rest_framework import serializers
from categories.models import Category
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
  name = models.CharField(max_length=100)
  image = serializers.ImageField(max_length=None, use_url=True, allow_empty_file=True, required=False)
  class Meta:
    fields = [
      'id',
      'name',
      'image'
      ]
    model = Category
