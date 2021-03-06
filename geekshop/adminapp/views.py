from unicodedata import category
from adminapp.forms import RegisterForm, UserChangeForm
from authapp.models import ShopUser
from adminapp.forms import CategoryEditForm
from mainapp.models import Category, Product
from adminapp.utils import check_is_superuser
from django.contrib.auth.decorators import user_passes_test
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


@check_is_superuser
def users(request):
    return render(request, "adminapp/users.html", context={
        "title": "Пользователи",
        "users": ShopUser.objects.filter(is_active=True)
    })

@check_is_superuser
def update_user(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    form = UserEditForm(instance=user)
    
    if request.method == 'POST':
        form = UserEditForm(
            instance=user, 
            data=request.POST, 
            files=request.FILES
        )
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:users'))
            
    return render(request, 'adminapp/update_user', context={
            'title': 'Редактирование пользователя',
            'user': user,
            'form': form
        })

@check_is_superuser
def delete_user(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin:users'))
    

@check_is_superuser
def create_user(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:users'))
            
    return render(request, 'adminapp/create_user.html', context={
            'title': 'Создание пользователя',
            'form': form
        }
    )

@check_is_superuser
def create_category(request):
    form = CategoryEditForm()
    
    if request.method == 'POST':
        form = CategoryEditForm(data=request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:categories'))
            
    return render(request, 'adminapp/create_category.html', context={
            'title': 'Создание категории',
            'form': form
        }
    )

@check_is_superuser
def categories(request):
    return render(request, "adminapp/categories.html", context={
        "title": "Категории",
        "categories": Category.objects.filter(is_active=True)
    })

@check_is_superuser
def update_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryEditForm(instance=category)
    
    if request.method == 'POST':
        form = CategoryEditForm(
            instance=category, 
            data=request.POST, 
        )
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('admin:categories'))
            
    return render(request, 'adminapp/update_category.html', context={
            'title': 'Редактирование категории',
            'category': category,
            'form': form
        },
    )



@check_is_superuser
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admin:categories'))

@check_is_superuser
def create_product(request, pk):
    pass

@check_is_superuser
def products(request, pk):
    category= get_object_or_404(Category, pk=pk)
    return render(request, "adminapp/products.html", context={
        "title": f"Категория: {category.name}",
        "products": Product.objects.filter(category=category)
    })

@check_is_superuser
def update_product(request, pk):
    pass

@check_is_superuser
def delete_product(request, pk):
    pass

