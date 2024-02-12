from django.db import models
from api.models.model import AbstractCreatedByHelper

class Alert(AbstractCreatedByHelper):
    message = models.TextField()
    message_from = models.CharField(max_length=255)
    # user_detail = models.ForeignKey('UserDetail', on_delete=models.CASCADE)
    


    class Meta:
        db_table = 'ALERT'
