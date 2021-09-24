from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import BigIntegerField

class SmsUser(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False, blank=True)
    sms_count = models.BigIntegerField()

    def __str__(self):
        return self.email


class SmsLogModel(models.Model):
    user_id = models.UUIDField(unique=True)
    message  = ArrayField(ArrayField(models.CharField(max_length=100)))
    count = models.IntegerField(null=True)
    contact_no = ArrayField(BigIntegerField(models.BigIntegerField()))

    def __str__(self):
        return self.user_id
