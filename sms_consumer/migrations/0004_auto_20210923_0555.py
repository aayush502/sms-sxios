# Generated by Django 3.2.6 on 2021-09-23 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_consumer', '0003_smsuser_sms_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsuser',
            name='sms_count',
            field=models.BigIntegerField(),
        ),
        migrations.CreateModel(
            name='SmsLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=1000)),
                ('count', models.IntegerField()),
                ('contact_no', models.BigIntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_consumer.smsuser')),
            ],
        ),
    ]