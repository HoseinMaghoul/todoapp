# Generated by Django 3.2.6 on 2021-10-05 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20211005_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 10, 21, 10, 311029, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 10, 21, 10, 311075, tzinfo=utc)),
        ),
    ]