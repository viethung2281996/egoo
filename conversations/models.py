import uuid
from django.db import models
from units.models import Unit
from egoo_core.storage import OverwriteStorage

# Create your models here.
class Conversation(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  context = models.TextField(null=False, blank=False)
  image = models.TextField(null=True, blank=True)
  audio = models.TextField(null=True, blank=True)
  order = models.IntegerField(null=False)
  is_robot = models.BooleanField(default=False)
  recommend = models.TextField(null=True, blank=True)
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    related_name='list_conversation',
    )

  def __str__(self):
    return "Conversation: %s" % self.id

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("conversation", self.id)