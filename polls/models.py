from django.db import models
from django.contrib.postgres.fields import ArrayField

from users.models import User
from posts.models import Post

class Poll(models.Model):
    title = models.TextField()
    options = ArrayField(models.CharField(max_length=255))
    votes = ArrayField(models.IntegerField(default=0))
    
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='attached_polls')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_polls')
    voted = models.ManyToManyField(User, related_name='voted_polls')

    is_approved = models.BooleanField(default=False)
