# from unicodedata import name
from django.contrib import admin
from django.urls import path
from Mandi import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]

