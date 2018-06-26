from django.db import models
from units.models import Unit
# Create your models here.
class Note(models.Model):
  text = models.TextField(null=False, blank=False)
  pronounce = models.TextField(null=False, blank=False)
  audio = models.TextField(null=False, blank=False)
  units = models.ManyToManyField(Unit)

  def __str__(self):
    return "Note: %s" % self.id