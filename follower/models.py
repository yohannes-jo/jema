from django.db import models

from profiles.models import Profile

class Follower(models.Model):
    followed_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='followed_by'
    )
    following = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        unique_together = ('followed_by', 'following')

    def __str__(self):
        return f"{self.followed_by.username} is following {self.following.username}"