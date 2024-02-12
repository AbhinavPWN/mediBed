from django.db import models
from api.models.abstractClass import AbstractProfile

class Patient(AbstractProfile):
    address = models.CharField(max_length=255)
    other_details = models.TextField()
    hospital = models.ForeignKey('HOSPITAL', on_delete=models.CASCADE)

    class Meta:
        db_table = 'PATIENT'
