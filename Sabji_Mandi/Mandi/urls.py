
from django.contrib import admin
from django.urls import path
from Mandi import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('viewcart/', views.viewcart, name="viewcart"),
    path('about/', views.about, name="about"),
    path('first/', views.homep, name=""),
]

