from units.models import Unit
from django.db import models
from categories.models import Category
from rest_framework import serializers
from categories.serializers import CategorySerializer

class UnitSerializer(serializers.HyperlinkedModelSerializer):
  category = CategorySerializer(read_only=True)
  category_id = models.IntegerField(null=False)

  def create(self, validated_data):
    import pdb; pdb.set_trace()
    category = Category.objects.get(pk=validated_data["category_id"])
    unit = Unit.objects.create(
        title = validated_data["title"],
        order = validated_data["order"],
        category = category
      )
   
    if unit.save():
      return unit

  class Meta:
    fields = (
      'id',
      'title',
      'order',
      'category',
      'category_id'
      )
    model = Unit
    depth=1