from django.shortcuts import render, redirect
from .models import Request
from django.http import HttpResponse
import bcrypt
from django.contrib import messages
from django.contrib.auth.hashers import check_password 

# Create your views here.
def Request (request, *args, **kwargs):
    return render(request, "requests.html", {})

def Sign_out(request, *args, **kwargs):
    return render(request, "sign_out.html", {})

def Contact_us(request, *args,**kwargs):
    return render(request, "about_us.html", {})