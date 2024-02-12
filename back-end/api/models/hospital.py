from django.db import models
from api.models.abstractClass import AbstractCodeHelper

class Hospital(AbstractCodeHelper):
    location= models.ForeignKey('LOCATION', on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'HOSPITAL'
    

