from django.db import models

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status_desc = models.CharField(max_length=45)
    icon = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'STATUS'
