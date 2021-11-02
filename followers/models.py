from django.db import models

from django.contrib.auth.models import User

class Follower(models.Model):
    """Signifies one 'User' following aother."""

    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    def __str__(self):
        return f"{self.follower.username} is following {self.following.username}"