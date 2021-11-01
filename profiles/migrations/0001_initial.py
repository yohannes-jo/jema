# Generated by Django 3.2.8 on 2021-10-31 07:31

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True)),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='profiles')),
                ('password', models.CharField(blank=True, max_length=64)),
                ('bio', models.TextField()),
            ],
        ),
    ]
