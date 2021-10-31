from django.db import models
from django.db.models.fields.files import FileField
from sorl.thumbnail import ImageField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    username = models.CharField(max_length=32, null=False, blank=False)
    email = models.EmailField(null=False)
    image = ImageField(upload_to='profiles')
    password = models.CharField(max_length=64, null=False, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.username