from dataclasses import fields
from pyexpat import model
from django import forms
from .models import ShopUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

class LoginForm(AuthenticationForm):
    pass

class RegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ("username",)

class UserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'age')
    
 #   def clean_city():
 #       pass
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "password":
                field.widget = forms.HiddenInput()
                 
    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data