from django.db import models
from services.abstractSchema.adminInfo import AdminInfo

class TimeStampedModel(AdminInfo):
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True