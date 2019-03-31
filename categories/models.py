import uuid
from django.db import models
from commons.models import BaseModel

# Create your models here.
CODE_STATUS_CHOICE = (
  ('Active', 'Active'),
  ('Used', 'Used'),
  )

CODE_TYPE_CHOICE = (
  ('Free', 'Free'),
  ('Payment', 'Payment'),
  )

CATEGORY_TYPE_CHOICE = (
  ('Free', 'Free'),
  ('Licences', 'Licences'),
  )

class Category(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100, unique=True)
  order = models.IntegerField(null=False, unique=True)
  image = models.TextField(null=True, blank=True)
  type = models.CharField(null=False, max_length=20, choices=CATEGORY_TYPE_CHOICE, default='Free')
  base_price = models.CharField(max_length=100, default='0')

  def __str__(self):
    return "Category: %s" % self.name

  def init_file_name(self, file):
    if file is None:
      return ""
    else:
      return "{0}_{1}".format("category", self.id)

  def get_unit_ids(self):
    units = self.list_unit.all()
    return list(map(lambda unit: str(unit.id), units))

  def get_total_score_of_user(self, user_id):
    units = self.list_unit.all()
    #get score array with unit array
    scores = list(map(lambda unit: unit.get_max_score_of_user(user_id), units))

    return sum(scores)

class ActivationCode(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  code = models.CharField(max_length=10, unique=True)
  status = models.CharField(null=False, max_length=20, choices=CODE_STATUS_CHOICE, default='Active')
  type = models.CharField(null=False, max_length=20, choices=CODE_TYPE_CHOICE, default='Free')
  time = models.DurationField(default=None, null=True)
  category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='activation_codes',
    )