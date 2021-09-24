from django.contrib import admin
from . import models

class AdminArea(admin.AdminSite):
    site_header = "Sms Admin Panel"

sms_site = AdminArea(name="Admin Area")

sms_site.register(models.SmsUser)
sms_site.register(models.SmsLogModel)