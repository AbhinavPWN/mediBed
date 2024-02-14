from django.db import models

class AdminInfo(models.Model):
    created_by_admin = models.ForeignKey('Admin', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_created_by_admin')
    updated_by_admin = models.ForeignKey('Admin', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_updated_by_admin')
    deleted_by_admin = models.ForeignKey('Admin', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_deleted_by_admin')

    class Meta:
        abstract = True