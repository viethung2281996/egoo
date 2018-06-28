from rest_framework import serializers
from category.models import Category
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
  name = models.CharField(max_length=100)
  class Meta:
    fields = [
      'id',
      'name'
      ]
    model = Category
