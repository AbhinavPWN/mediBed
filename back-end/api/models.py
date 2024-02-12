from django.db import models

class AbstractEntity(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True

class AbstractStatusHelper(AbstractEntity):
    status = models.ForeignKey('STATUS', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class AbstractUpdatedByHelper(AbstractStatusHelper):
    last_updated_date = models.DateTimeField(auto_now=True)
  #  updated_by_admin = models.ForeignKey('ADMIN', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_updated_by_admin')

    class Meta:
        abstract = True

class AbstractCreatedByHelper(AbstractUpdatedByHelper):
    created_date = models.DateTimeField(auto_now_add=True)
 #   created_by_admin = models.ForeignKey('ADMIN', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_created_by_admin')

    class Meta:
        abstract = True

class AbstractDeletedByHelper(AbstractCreatedByHelper):
    deleted_date = models.DateTimeField(null=True, blank=True)
 #   deleted_by_admin = models.ForeignKey('ADMIN', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_deleted_by_admin')
    deleted_reason = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

class AbstractProfile(AbstractCreatedByHelper):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        abstract = True

class AbstractBlockUnblockHelper(AbstractDeletedByHelper):
    id = models.OneToOneField(AbstractDeletedByHelper, primary_key=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class AbstractCodeHelper(AbstractProfile):
    code = models.CharField(max_length=255)

    class Meta:
        abstract = True

# class AbstractUser(AbstractBlockUnblockHelper):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     username = models.CharField(max_length=150, unique=True)
#     wrong_password_attempt = models.PositiveIntegerField(default=0)
#     last_logged_in_time = models.DateTimeField(null=True, blank=True)
#     blocked_id = models.ForeignKey(AbstractBlockUnblockHelper, on_delete=models.CASCADE, null=True, blank=True)

#     class Meta:
#         abstract = True

class Hospital(AbstractCodeHelper):
    location= models.ForeignKey('LOCATION', on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'HOSPITAL'

class Location(AbstractCreatedByHelper):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zipcode = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'LOCATION'

class Patient(AbstractProfile):
    address = models.CharField(max_length=255)
    other_details = models.TextField()
    hospital = models.ForeignKey('HOSPITAL', on_delete=models.CASCADE)

    class Meta:
        db_table = 'PATIENT'

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status_desc = models.CharField(max_length=45)
    icon = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        db_table = 'STATUS'

class ICU(AbstractDeletedByHelper):
  
    hospital = models.ForeignKey('HOSPITAL', on_delete=models.CASCADE)
    no_of_ward = models.PositiveIntegerField(default=0)
    is_vacant = models.BooleanField(default=True)

    class Meta:
        db_table = 'ICU'

# class Admin(AbstractUser):
#     is_super_admin = models.BooleanField(default=False) 
#     is_central_admin = models.BooleanField(default=False)


#     class Meta:
#         db_table = 'ADMIN'

class Ambulance(AbstractProfile):
    vehicle_number = models.CharField(max_length=50, unique=True)
    ambulance_number = models.CharField(max_length=50)
    hospital = models.ForeignKey('HOSPITAL', on_delete=models.CASCADE)

    class Meta:
        db_table = 'AMBULANCE'

class Alert(AbstractCreatedByHelper):
    message = models.TextField()
    message_from = models.CharField(max_length=255)
    # user_detail = models.ForeignKey('UserDetail', on_delete=models.CASCADE)
    


    class Meta:
        db_table = 'ALERT'
























