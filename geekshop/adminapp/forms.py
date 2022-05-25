from dataclasses import fields
from pyexpat import model
from django import forms
from authapp.models import ShopUser
from mainapp.models import Category
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'age')

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'age')
    
class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'