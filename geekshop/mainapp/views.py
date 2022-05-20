
from django.shortcuts import render
from django.urls import reverse
import json
from .models import Product, Category


with open('data.txt') as json_file:
    product_list = json.load(json_file)

MENU_LINKS = {
    "index": "Главная",
    "products": "Продукты",
    "contact": "Контакты",
}


def main(request):
    return render(request, "mainapp/index.html", context={
        "title": "Главная",
        "menu": MENU_LINKS,
    })


def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()[4:7]
    return render(request, "mainapp/products.html", context={
        "title": "Продукты",
        "menu": MENU_LINKS,
        "products": products,
        "categories": categories,
    })


def contact(request):
    return render(request, "mainapp/contact.html", context={
        "title": "Контакты",
        "menu": MENU_LINKS,
    })
