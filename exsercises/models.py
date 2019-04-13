import uuid
from django.db import models
from commons.models import BaseModel
from units.models import Unit
from jsonfield import JSONField

EXSERCISE_TYPE = (
  ('LISTEN_AND_READ', 'LISTEN_AND_READ'),
  ('CHOSE_ANSWER', 'CHOSE_ANSWER'),
  ('REWRITE_SENTENCE', 'REWRITE_SENTENCE'),
  ('TRANSLATE_SENTENCE', 'TRANSLATE_SENTENCE'),
  )

class Exsercise(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  type = models.CharField(null=False, max_length=50, choices=EXSERCISE_TYPE)
  order = models.IntegerField(null=False, default=1)
  
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE
    )

  def init_file_name(self, file):
    return "" if file is None else "{0}_{1}".format("exsercise", self.id)

class ListenAndReadExsercise(Exsercise):
  image = models.TextField(null=True, blank=True)
  answer = models.TextField(null=True, blank=True)
  audio = models.TextField(null=True, blank=True)
  explain = models.TextField(null=True, blank=True)

class ChoseAnswerExsercise(Exsercise):
  image = models.TextField(null=True, blank=True)
  audio = models.TextField(null=True, blank=True)
  chose_answers = JSONField(default={}) # array field
  answer = models.TextField(null=True, blank=True)
  explain = models.TextField(null=True, blank=True)

class RewriteSentenceExsercise(Exsercise):
  phrases = JSONField(default={}) # json field
  answer = models.TextField(null=True, blank=True)
  audio = models.TextField(null=True, blank=True)
  explain = models.TextField(null=True, blank=True)

class TranslateSentenceExsercise(Exsercise):
  sentence = models.TextField(null=True, blank=True)
  answer = models.TextField(null=True, blank=True)
  image = models.TextField(null=True, blank=True)
  explain = models.TextField(null=True, blank=True)
