
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Mandi import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('viewcart/', views.viewcart, name="viewcart"),
    path('about/', views.about, name="about"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.homepage, name="home"),
    path("update/<customer_id>", views.update, name="update"),
    path('allproduct/', views.allproduct, name="allproduct"),
    path('buypage/<slug:p_id>', views.order, name="orderpage"),
    path('buyfinal', views.buyfinal ,name="buyfinal"),


]
