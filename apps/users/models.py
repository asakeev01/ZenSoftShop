from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from apps.products.models import *


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="favorite")
    products = models.ManyToManyField(Product, related_name="favorites")

    def __str__(self):
        return f"{self.user.username}'s favorites"


@receiver(post_save, sender=User)
def create_favorite(sender, instance, created, **kwargs):
    if created:
        Favorite.objects.create(user=instance)





