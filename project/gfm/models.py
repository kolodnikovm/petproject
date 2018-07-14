from django.db import models
from users.models import User


class WishList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, related_name='wishlists', on_delete=models.CASCADE)


class WishListItem(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    description = models.TextField()
    wishlist = models.ForeignKey(
        WishList, related_name='items', on_delete=models.CASCADE)
