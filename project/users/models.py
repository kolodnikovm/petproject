from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField()
    friends = models.ManyToManyField('self', related_name='friends')

    def __str__(self):
        return self.username


class Friendship(models.Model):
    pass


class UserGroups(models.Model):
    name = models.CharField(max_length=100)
    # TODO Допилить группы
