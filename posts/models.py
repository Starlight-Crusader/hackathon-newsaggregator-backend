from django.db import models
from tags.models import Tag

class Post(models.Model):
    timestamp = models.TimeField()
    title = models.TextField()
    body = models.TextField()
    link = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)
