# Generated by Django 5.1.6 on 2025-03-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_character_user_alter_character_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
