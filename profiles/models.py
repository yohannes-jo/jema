from django.db import models
from django.contrib.auth.models import User

from sorl.thumbnail import ImageField

class Profile(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    picture = ImageField(upload_to='profiles')
    bio = models.TextField()

    # Has relation with the 'User' model
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user',
    )

    def __str__(self):
        return self.user.username

