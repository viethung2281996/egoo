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
  title = models.CharField(null=False, max_length=100)
  order = models.IntegerField(null=False)
  image = models.ImageField(upload_to='units/images/', null=True, storage=OverwriteStorage())
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