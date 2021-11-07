from django.contrib.auth.models import User
from django.db import models

from profiles.models import Profile

class Post(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts/")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.author.username}: {self.caption}"

class Comment(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='text',
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='author',
    )