from django.db import models
from users.models import User


class Gift(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=300, blank=True)
    picture = models.ImageField()
