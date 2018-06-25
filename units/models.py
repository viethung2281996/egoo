from django.db import models
from categories.models import Category
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