from rest_framework import serializers
from units.models import Unit
from .models import Reading, Question

class QuestionSerializer(serializers.ModelSerializer):
  reading = serializers.PrimaryKeyRelatedField(many=False, queryset=Reading.objects.all())
  chose_answers = serializers.DictField(child=serializers.CharField())

  class Meta:
    fields = (
      'question',
      'chose_answers',
      'answer',
      'order',
      'reading'
      )
    model = Question

class ReadingSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())
  questions = QuestionSerializer(many=True, read_only=True)

  class Meta:
    fields = (
      'id',
      'content',
      'unit',
      'questions',
      )
    model = Reading
