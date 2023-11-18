from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from tags.models import Tag


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255)

    subscriptions = models.ManyToManyField(Tag, related_name='subscribers', blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
