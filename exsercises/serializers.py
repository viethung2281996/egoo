from rest_framework import serializers 
from .models import Exsercise, ListenAndReadExsercise, ChoseAnswerExsercise, RewriteSentenceExsercise, TranslateSentenceExsercise
from units.models import Unit
from enum import Enum

class PolymorphicSerializer(serializers.Serializer):
    def get_serializer_map(self):
        raise NotImplementedError

    def get_instance_map(self):
        raise NotImplementedError

    def to_representation(self, obj):
        type_str = obj.type

        try:
            serializer = self.get_serializer_map()[type_str]
        except KeyError:
            raise ValueError('Serializer for "{}" does not exist'.format(type_str), )

        try:
            instance = self.get_instance_map()[type_str].objects.get(id=obj.id)
        except KeyError:
            raise ValueError('Instance for "{}" does not exist'.format(type_str), )

        data = serializer(instance).data
        return data

    def to_internal_value(self, data):
        try:
            type_str = data['type']
        except KeyError:
            raise serializers.ValidationError({
                'type': 'This field is required',
            })

        try:
            serializer = self.get_serializer_map()[type_str]
        except KeyError:
            raise serializers.ValidationError({
                'type': 'Serializer for "{}" does not exist'.format(type_str),
            })

        validated_data = serializer(context=self.context).to_internal_value(data)
        validated_data['type'] = type_str
        return validated_data

    def create(self, validated_data):
        serializer = self.get_serializer_map()[validated_data['type']]
        validated_data.pop('type')
        return serializer(context=self.context).create(validated_data)

    def update(self, instance, validated_data):
        serializer = self.get_serializer_map()[validated_data['type']]
        validated_data.pop('type')
        return serializer(context=self.context).update(instance, validated_data)

class ExserciseSerializer(PolymorphicSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())

  class Meta:
    model = Exsercise

  def get_serializer_map(self):
    return {
      'LISTEN_AND_READ': ListenAndReadExserciseSerializer,
      'CHOSE_ANSWER': ChoseAnswerExserciseSerializer,
      'REWRITE_SENTENCE': RewriteSentenceExserciseSerializer,
      'TRANSLATE_SENTENCE': TranslateSentenceExserciseSerializer,
    }
  def get_instance_map(self):
    return {
      'LISTEN_AND_READ': ListenAndReadExsercise,
      'CHOSE_ANSWER': ChoseAnswerExsercise,
      'REWRITE_SENTENCE': RewriteSentenceExsercise,
      'TRANSLATE_SENTENCE': TranslateSentenceExsercise,
    }

class ListenAndReadExserciseSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())

  def validate(self, data):
    if self.instance is None:
      exercise_orders = map(lambda x: x.order, data['unit'].exsercise_set.all())
      if data['order'] in exercise_orders:
        raise serializers.ValidationError("Order of exsercise must unique in unit")
    return data

  class Meta:
    fields = (
      'id',
      'type',
      'order',
      'image',
      'audio',
      'answer',
      'explain',
      'unit',
      )
    model = ListenAndReadExsercise

class ChoseAnswerExserciseSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())
  chose_answers = serializers.DictField(child=serializers.CharField())

  def validate(self, data):
    if self.instance is None:
      exercise_orders = map(lambda x: x.order, data['unit'].exsercise_set.all())
      if data['order'] in exercise_orders:
        raise serializers.ValidationError("Order of exsercise must unique in unit")
    return data

  class Meta:
    fields = (
      'id',
      'type',
      'order',
      'image',
      'audio',
      'chose_answers',
      'answer',
      'explain',
      'unit',
      )
    model = ChoseAnswerExsercise

class RewriteSentenceExserciseSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())
  phrases = serializers.ListField(child=serializers.DictField())

  def validate(self, data):
    if self.instance is None:
      exercise_orders = map(lambda x: x.order, data['unit'].exsercise_set.all())
      if data['order'] in exercise_orders:
        raise serializers.ValidationError("Order of exsercise must unique in unit")
    return data

  class Meta:
    fields = (
      'id',
      'type',
      'order',
      'phrases',
      'answer',
      'audio',
      'explain',
      'unit'
      )
    model = RewriteSentenceExsercise

class TranslateSentenceExserciseSerializer(serializers.ModelSerializer):
  unit = serializers.PrimaryKeyRelatedField(many=False, queryset=Unit.objects.all())

  def validate(self, data):
    if self.instance is None:
      exercise_orders = map(lambda x: x.order, data['unit'].exsercise_set.all())
      if data['order'] in exercise_orders:
        raise serializers.ValidationError("Order of exsercise must unique in unit")
    return data

  class Meta:
    fields = (
      'id',
      'type',
      'image',
      'order',
      'sentence',
      'answer',
      'explain',
      'unit'
      )
    model = TranslateSentenceExsercise