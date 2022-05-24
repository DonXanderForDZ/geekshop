from audioop import reverse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from .models import Basket

# Create your views here.

def view (request):
    render(request, 'basketapp/view.html')

def add (request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('index')))

def remove (request, basket_id):
    basket = get_object_or_404(Basket, pk=basket_id)
    basket.delete
    return HttpResponseRedirect(reverse('basket:view'))