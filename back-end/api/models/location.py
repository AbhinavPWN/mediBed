from django.db import models
from api.models.abstractClass import AbstractCreatedByHelper

class Location(AbstractCreatedByHelper):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'LOCATION'
