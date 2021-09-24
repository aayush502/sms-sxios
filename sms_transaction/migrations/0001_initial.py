# Generated by Django 3.2.6 on 2021-09-21 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sms_consumer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sms_in', models.IntegerField()),
                ('sms_out', models.IntegerField()),
                ('date', models.DateField(default=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_consumer.smsuser')),
            ],
        ),
    ]
