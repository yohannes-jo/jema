# Generated by Django 3.2.8 on 2021-10-30 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_profile_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='image',
        ),
    ]
