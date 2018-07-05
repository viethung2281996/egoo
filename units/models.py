import uuid
from django.db import models
from categories.models import Category
from egoo_core.storage import OverwriteStorage
#Create your models here.
LEVEL_CHOICE = (
  ('Elementary', 'Elementary'),
  ('Intermediate', 'Intermediate'),
  ('Advanced', 'Advanced'),
  ('Proficient', 'Proficient'),
  )

class Unit(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(null=False, max_length=100, unique=True)
  order = models.IntegerField(null=False, unique=True)
  image = models.TextField(null=True, blank=True)
  level = models.CharField(null=False, max_length=12, choices=LEVEL_CHOICE, default='Elementary')
  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='list_unit',
    null=True,
    blank=True
    )

  def __str__(self):
    return "Unit: %s" % self.title  

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("unit", self.id)