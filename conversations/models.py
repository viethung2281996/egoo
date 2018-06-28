from django.db import models
from units.models import Unit
from egoo_core.storage import OverwriteStorage

# Create your models here.
class Conversation(models.Model):
  context = models.TextField(null=False, blank=False)
  image = models.ImageField(upload_to='conversations/images/', null=True, storage=OverwriteStorage())
  audio = models.FileField(upload_to='conversations/audios/', null=True, storage=OverwriteStorage())
  order = models.IntegerField(null=False)
  is_robot = models.BooleanField(default=False)
  recommend = models.CharField(max_length=20, blank=True, default='')
  unit = models.ForeignKey(
    Unit,
    on_delete=models.CASCADE,
    related_name='list_conversation',
    )

  def __str__(self):
    return "Conversation: %s" % self.id
