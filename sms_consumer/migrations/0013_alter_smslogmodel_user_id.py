# Generated by Django 3.2.7 on 2021-09-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_consumer', '0012_auto_20210924_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslogmodel',
            name='user_id',
            field=models.UUIDField(unique=True),
        ),
    ]
