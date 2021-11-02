from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm




class UserRegister(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model= User
        fields=['username', 'email', 'password1', 'password2']

class idApplicationForm(ModelForm):
    email=forms.EmailField()

    class Meta:
        model= ApplicationID
        fields= "__all__"


class passportApplicationForm(ModelForm):
    email=forms.EmailField()

    class Meta:
        model= ApplicationPassport
        fields = "__all__"

