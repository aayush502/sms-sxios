# Generated by Django 3.2.7 on 2021-09-24 04:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_consumer', '0010_alter_smslogmodel_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslogmodel',
            name='contact_no',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), size=None), size=None),
        ),
    ]
