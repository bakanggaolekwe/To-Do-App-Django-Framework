# Generated by Django 4.0.2 on 2022-03-08 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated_timestamp',
        ),
    ]
