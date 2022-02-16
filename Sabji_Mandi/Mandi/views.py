from urllib import request
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *
from django.contrib import messages


# Create your views here.

def homepage(request):
    username = request.session['username']
    user = Customer.objects.get(username = username)

    return render(request, 'homepage.html', {'user':user})


def register(request):
    if request.method == "POST":
        form = Customer_form(request.POST)
        username = request.POST['username']
        if form.is_valid():
            if Customer.objects.filter(username=username).exists():
                messages.error("Username already exists")
                return redirect("/register/")
            else:
                form.save()
                return redirect("/login/")

    return render(request, 'registration/regis.html')

def login(request):
    if request.method == "POST":
        username = request.session['username'] = request.POST['username']
        password = request.session['password'] = request.POST['password']
        user = Customer.objects.get(username = username, password = password)
        if user is not None:
            Customer.objects.filter(username = username).update(is_login = True)
            return redirect("/home")
        else:
            return redirect("/login")

    return render(request, 'login/login.html')


def contact(request):
    return render(request, 'contact/contact.html')

def viewcart(request):
    return render(request, 'viewCart/viewcart.html')


def about(request):
    return render(request, 'about/about.html')

def logout(request):
    request.session.flush()
    return redirect("/")

def home(request):
    return render(request, 'homepage.html')

def update(request, customer_id):
    user = Customer.objects.get(customer_id = customer_id)
    if request.method == "POST":
        forms = Customer_form(request.POST, request.FILES, instance= user)
        forms.save()
        return redirect("/login/")
    
    return render(request,'update/update_profile.html', {'user':user})

