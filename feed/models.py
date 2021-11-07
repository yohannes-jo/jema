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

class Like(models.Model):
    date_added = models.DateTimeField(auto_now=True)

    by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='liker',
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='liked_post',
    )

    def __str__(self):
        return f"{self.by.user.username} has liked a post made by {self.post.author.user.username}."

class Comment(models.Model):
    date_added = models.DateTimeField(auto_now=True)

    by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='commenter',
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='commented_post',
    )

    text = models.CharField(max_length=140, null=True, blank=True,)

    def __str__(self):
        return f"{self.by.user.username}'s comment on {self.post.author.user.username}'s post: {self.text[:50]}"

class Share(models.Model):
    date_added = models.DateTimeField(auto_now=True)

    by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='sharer',
    )

    to = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='target',
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='shared_post'
    )

    def __str__(self):
        return f"From {self.by.user.username} has shared a post to {self.to.user.username}."