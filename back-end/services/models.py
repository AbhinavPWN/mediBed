from django.db import models
from services.abstractSchema.abstractTimeStamp import TimeStampedModel

class Admin(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150, unique=True)
    wrong_password_attempt = models.PositiveIntegerField(default=0)
    last_logged_in_time = models.DateTimeField(null=True, blank=True)
    is_super_admin = models.BooleanField(default=False)
    is_central_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'createAdmin'



class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status_desc = models.CharField(max_length=45)
    icon = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'status'

class Location(TimeStampedModel):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'location'

class Hospital(TimeStampedModel):
    code = models.CharField(max_length=255)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    class Meta:
        db_table = 'hospital'

class ICU(TimeStampedModel):
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    no_of_ward = models.PositiveIntegerField(default=0)
    is_vacant = models.BooleanField(default=True)

    class Meta:
        db_table = 'icu'

class Ambulance(TimeStampedModel):
    vehicle_number = models.CharField(max_length=50, unique=True)
    ambulance_number = models.CharField(max_length=50)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    class Meta:
        db_table = 'ambulance'

class Patient(TimeStampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, blank=True, null=True)
    address = models.CharField(max_length=255)
    other_details = models.TextField()
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    class Meta:
        db_table = 'patient'


class Alert(TimeStampedModel):
    message = models.TextField()
    message_from = models.CharField(max_length=255)

    class Meta:
        db_table = 'alert'
