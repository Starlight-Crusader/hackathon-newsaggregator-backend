from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from categories.models import Category


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True, max_length=255)

    subscriptions = models.ManyToManyField(Category, related_name='subscribers', blank=True)

    USERNAME_FIELD = 'username'
