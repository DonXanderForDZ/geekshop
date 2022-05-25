from distutils.command.upload import upload
from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=140)


def __str__(self):
    return f'{self.id}: {self.name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quatity = models.PositiveIntegerField(default=0)


def __str__(self):
    return f'{self.id}: {self.name}'
