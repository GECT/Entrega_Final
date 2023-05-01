from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Product, Wallpaper

class UserRegistrationForm(UserChangeForm):
    email = forms.CharField()
    password1 = forms.CharField(label="Password: ", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password: ", widget=forms.PasswordInput)
    class Meta():
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_tex = {k:"" for k in fields}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'detail', 'price', 'image')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Wallpaper
        fields = ['name', 'image']
