# Generated by Django 2.0.2 on 2018-03-20 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180320_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='datepulished',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 20, 15, 23, 28, 622041, tzinfo=utc)),
        ),
    ]
