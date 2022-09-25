from email.policy import default
from hashlib import blake2b
from operator import mod
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    sort_name = models.CharField(max_length=10, null=True, blank=True)
    contact_number = PhoneNumberField(max_length=14, null=True, blank=True)
    profile_pic = models.ImageField(default="user.png", null=True, blank=True)

    def __str__(self):
        return self.sort_name

class ExtraAdd(models.Model):
    position = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.position

class DropYou(models.Model):
    person = models.ForeignKey(UserProfile, null=True, blank=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True)
    position = models.ForeignKey(ExtraAdd, null=True, blank=True, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True)
    text = models.TextField(max_length=10000, null=True, blank=True)


    def __str__(self):
        return self.name



