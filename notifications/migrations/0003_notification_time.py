# Generated by Django 3.2.9 on 2021-11-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20211104_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
