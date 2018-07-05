from django.db import models
import uuid
from units.models import Unit
from egoo_core.storage import OverwriteStorage

# Create your models here.
class Note(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  text = models.TextField(null=False, blank=False)
  pronounce = models.TextField(null=False, blank=False)
  audio = models.TextField(null=True, blank=True)
  units = models.ManyToManyField(Unit)

  def __str__(self):
    return "Note: %s" % self.id

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("notes", self.id)