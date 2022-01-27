from urllib import request
from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')
    
def register(request):
    return render(request, 'registration/regis.html')

def login(request):
    return render(request, 'login/login.html')