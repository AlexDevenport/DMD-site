# Generated by Django 5.1.6 on 2025-03-09 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
