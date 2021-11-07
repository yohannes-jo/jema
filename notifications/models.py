from django.db import models

from profiles.models import Profile


class Notification(models.Model):
    notifier = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='notifier',
        null=True,
        blank=True,
    )

    notified_to = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='notified_to',
        null=True,
        blank=True,
    )

    caption = models.CharField(max_length=80, null=True, blank=True,)
    time = models.DateTimeField(auto_now=True)
    # TODO: change this later
    def __str__(self):
        return f"{self.notifier.user.username} to {self.notified_to.user.username}: {self.caption}"

