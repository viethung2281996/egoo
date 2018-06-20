from units.models import Unit
from rest_framework import serializers
from categories.serializers import CategorySerializer

class UnitSerializer(serializers.ModelSerializer):
  category = CategorySerializer(read_only=True)
  class Meta:
    fields = (
      'id',
      'title',
      'order',
      'category'
      )
    model = Unit