import uuid
from django.db import models
from jsonfield import JSONField

from commons.models import BaseModel
from units.models import Unit

class Reading(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  content = models.TextField(null=False, blank=False)
  
  unit = models.OneToOneField(
    Unit,
    on_delete=models.CASCADE
    )

class Question(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  question = models.TextField(null=True, blank=True)
  chose_answers = JSONField(default={}) # array field
  answer = models.TextField(null=True, blank=True)
  order = models.IntegerField(null=False, default=1)
  explain = models.TextField(null=True, blank=True)
  
  reading = models.ForeignKey(
    Reading,
    on_delete=models.CASCADE,
    related_name='questions'
    )