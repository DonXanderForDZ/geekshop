from itertools import product
from django.db import models
from mainapp.models import Product
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


def basket_sum(user):
    basket_item = Basket.objects.filter(user=user)
    return [item.product.price * item.quantity for item in basket_items]
