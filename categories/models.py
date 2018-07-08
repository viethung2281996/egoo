import uuid
from django.db import models
from egoo_core.storage import OverwriteStorage

# Create your models here.
class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100, unique=True)
  order = models.IntegerField(null=False, unique=True)
  image = models.TextField(null=True, blank=True)

  def __str__(self):
    return "Category: %s" % self.name

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("category", self.id)