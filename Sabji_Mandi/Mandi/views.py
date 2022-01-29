from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from .forms import *


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    print(request)
    if request.method == "POST":
            forms = customerForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('/login/')
            else:
                print(request)
    

    return render(request, 'registration/regis.html')


def login(request):
    return render(request, 'login/login.html')


def contact(request):
    return render(request, 'contact/contact.html')
