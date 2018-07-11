from django.db import models
from django.contrib.auth import get_user_model
from units.models import Unit
# Create your models here.
class Speaker(models.Model):
  user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='list_speaker',
    )
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    related_name='list_speaker',
    )
  score = models.IntegerField(null=False)

  def __str__(self):
    return "Speaker: %s" % self.id