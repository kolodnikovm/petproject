from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField()

    def __str__(self):
        return self.username
