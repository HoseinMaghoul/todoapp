# Generated by Django 3.2.6 on 2021-10-05 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='category',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='slug',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
