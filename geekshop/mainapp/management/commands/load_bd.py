from base64 import encode
from itertools import product
import json
import os
from unicodedata import name
from django.core.management.base import BaseCommand
from django.conf import settings
from mainapp.models import Category, Product
from django.contrib.auth import get_user_model


def load_from_json(file_name):
    with open(os.path.join('geekshop/json/' + file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):

    def handle(self, *args, **options):

        categories = load_from_json('categories')
        for category_data in categories:
            category = Category.objects.filter(name=category_data['name'])
            if not category:
                category = Category(**category_data)
                category.save()

        product = load_from_json('products')
        for product_data in product:
            product_data['category'] = Category.objects.get(
                name=product_data['category'])
            product = Product(**product_data)
            product.save()


User = get_user_model()
if not User.objects.filter(username='admin'):
    User.objects.create_superuser(username='admin', password='adminadmin')
