from django.db import models
from units.models import Unit

# Create your models here.
class Conversation(models.Model):
  context = models.TextField(null=False, blank=False)
  image = models.TextField(null=False, blank=False)
  audio = models.TextField(null=False, blank=False)
  order = models.IntegerField(null=False)
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    related_name='list_conversation',
    )

  def __str__(self):
    return "Conversation: %s" % self.id