from django.db import models
from units.models import Unit
from egoo_core.storage import OverwriteStorage

# Create your models here.
class Note(models.Model):
  text = models.TextField(null=False, blank=False)
  pronounce = models.TextField(null=False, blank=False)
  audio = models.FileField(upload_to='notes/audios/', null=True, storage=OverwriteStorage())
  units = models.ManyToManyField(Unit)

  def __str__(self):
    return "Note: %s" % self.id