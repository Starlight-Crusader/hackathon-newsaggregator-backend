from django.db import models
from users.models import User

class Petition(models.Model):
    title = models.TextField()
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_polls')
    voted = models.ManyToManyField(User, related_name='voted_polls')
