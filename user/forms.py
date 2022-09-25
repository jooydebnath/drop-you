from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class UserAddForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

# class UserChange(UserChangeForm):
#     class Meta:
#         fields = ['first_name', 'last_name', 'username', 'email']


class DropYouForm(ModelForm):
    class Meta:
        model = DropYou
        fields = '__all__'