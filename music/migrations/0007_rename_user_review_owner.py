# Generated by Django 3.2.23 on 2023-12-29 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_review_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='owner',
        ),
    ]
