from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    UPVOTE = 'UP'
    DOWNVOTE = 'DOWN'
    REACTION_CHOICES = (
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    )
    reaction = models.CharField(
        max_length=4,
        choices=REACTION_CHOICES,
        default=UPVOTE,
    )
