# Generated by Django 3.2.9 on 2021-11-02 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
