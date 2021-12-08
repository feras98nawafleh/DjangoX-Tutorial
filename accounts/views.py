from django.shortcuts import render
from django.views.generic import View
from .models import CustomUser
# Create your views here.

class AccountLogin(View):
    template_name = "account/login.html"
    model = CustomUser

class AccountSignUp(View):
    template_name = "account/signup.html"
    model = CustomUser