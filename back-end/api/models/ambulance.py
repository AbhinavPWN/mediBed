from django.db import models
from models.abstractClass import AbstractProfile

class Ambulance(AbstractProfile):
    vehicle_number = models.CharField(max_length=50, unique=True)
    ambulance_number = models.CharField(max_length=50)
    hospital = models.ForeignKey('HOSPITAL', on_delete=models.CASCADE)

    class Meta:
        db_table = 'AMBULANCE'
