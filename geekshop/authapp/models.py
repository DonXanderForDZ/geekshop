from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to="user_images", blank=True)
    age = models.DecimalField(max_digits=200, decimal_places=0, default=0, blank=True)
