import uuid
from django.db import models

from commons.models import BaseModel
from units.models import Unit

class Reading(BaseModel):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  content = models.TextField(null=False, blank=False)
  
  unit = models.OneToOneField(
    Unit,
    on_delete=models.CASCADE
    )
