from django.db import models
from api.models.abstractClass import AbstractDeletedByHelper

class ICU(AbstractDeletedByHelper):
  
    hospital = models.ForeignKey('HOSPITAL', on_delete=models.CASCADE)
    no_of_ward = models.PositiveIntegerField(default=0)
    is_vacant = models.BooleanField(default=True)

    class Meta:
        db_table = 'ICU'