# Generated by Django 3.2.23 on 2023-12-22 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='members',
        ),
    ]
