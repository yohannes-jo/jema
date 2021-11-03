from django.db import models

from profiles.models import Profile

class Message(models.Model):
    sender = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='sender',
    )
    reciever = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='reciever',
    )
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sender', 'reciever')

    def __str__(self):
        return f"{self.sender.user.username} to {self.reciever.user.username}: {self.text}"