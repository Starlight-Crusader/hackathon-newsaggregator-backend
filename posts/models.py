from django.db import models

class Post(models.Model):
    timestamp = models.TimeField()
    title = models.TextField()
    body = models.TextField()
