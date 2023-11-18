from django.db import models


TYPE_CHOICES = [
    (0, 'Default'),
    (1, 'Category'),
    (2, 'Region'),
]

class Tag(models.Model):
    type = models.IntegerField()
    name = models.CharField(max_length=255)
