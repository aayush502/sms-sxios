from django.db import models
from sms_consumer.models import *


class SmsTransaction(models.Model):
    user_id = models.ForeignKey(SmsUser, on_delete=models.CASCADE, null=False)
    sms_in = models.ForeignKey(SmsUser, related_name="smscount", on_delete=models.CASCADE)
    sms_out = models.IntegerField()
    date = models.DateField(default=True)
