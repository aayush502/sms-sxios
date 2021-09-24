# Generated by Django 3.2.7 on 2021-09-23 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_consumer', '0005_rename_msg_smslog_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmsLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('count', models.IntegerField()),
                ('contact_no', models.BigIntegerField()),
                ('hello', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_consumer.smsuser')),
            ],
        ),
        migrations.DeleteModel(
            name='SmsLog',
        ),
    ]