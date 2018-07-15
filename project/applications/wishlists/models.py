from django.db import models
from applications.users.models import User
from applications.gifts.models import Gift


class Wishlist(models.Model):
    name = models.CharField(max_length=140)
    owner = models.ForeignKey(
        User, related_name='wishlists', on_delete=models.CASCADE)
    gifts = models.ManyToManyField(Gift, related_name='wishlists')
