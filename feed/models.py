from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    caption = models.CharField(max_length=200)
    image = ImageField()