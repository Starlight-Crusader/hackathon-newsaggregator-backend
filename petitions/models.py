from django.db import models
from users.models import User

class Petition(models.Model):
    title = models.TextField()
    body = models.TextField()
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_posts')
    voted = models.ManyToManyField(User, related_name='voted_posts')
    
    is_approved = models.BooleanField(default=False)
