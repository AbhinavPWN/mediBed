from django.db import models
from api.models.abstractClass import AbstractUser

class Admin(AbstractUser):
    is_super_admin = models.BooleanField(default=False) 
    is_central_admin = models.BooleanField(default=False)


    class Meta:
        db_table = 'ADMIN'

