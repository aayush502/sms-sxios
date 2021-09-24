from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *
from django_select2 import forms as select2forms


class SmsForm(forms.ModelForm):
    class Meta:
        model = SmsUser
        fields = ["sms_count"]
        exclude = ('password', 'is_admin','email')

class SmsLogForm(forms.ModelForm):
    class Meta:
        model = SmsLogModel
        fields = ['contact_no', 'message']
        widgets={
            'contact_no': select2forms.Select2Widget
        }


