import uuid
from django.db import models
from commons.models import BaseModel
from units.models import Unit

# Create your models here.
class Guide(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  content = models.TextField(null=False, blank=False)
  video = models.TextField(null=True, blank=True)
  image = models.TextField(null=True, blank=True)

  unit = models.OneToOneField(
    Unit,
    on_delete=models.CASCADE
    )

  def __str__(self):
    return "Guide: %s" % self.id

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("guide", self.id)