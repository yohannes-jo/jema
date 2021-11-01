from django.db import models
from django.db.models.fields import DateTimeField
from profiles.models import Profile
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=500)
    time = DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    image = ImageField(upload_to='Post')

    def __str__(self):
        return self.text

