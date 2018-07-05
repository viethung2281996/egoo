from units.models import Unit, LEVEL_CHOICE
from django.db import models
from categories.models import Category
from notes.models import Note
from rest_framework import serializers

class UnitSerializer(serializers.ModelSerializer):
  category = serializers.PrimaryKeyRelatedField(many=False, queryset=Category.objects.all())
  note_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

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

