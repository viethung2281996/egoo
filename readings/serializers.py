from rest_framework import serializers
from units.models import Unit
from .models import Reading, Question

class QuestionSerializer(serializers.ModelSerializer):
  reading = serializers.PrimaryKeyRelatedField(many=False, queryset=Reading.objects.all())
  chose_answers = serializers.DictField(child=serializers.CharField())

  def validate(self, data):
    if self.instance is None:
      question_orders = map(lambda x: x.order, data['reading'].questions.all())
      if data['order'] in question_orders:
        raise serializers.ValidationError("Order of exsercise must unique in unit")
    return data

  class Meta:
    fields = (
      'id',
      'question',
      'chose_answers',
      'answer',
      'order',
      'explain',
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
