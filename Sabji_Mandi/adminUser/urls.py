
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.home,name="homeAdmin"),
    path('customer/',views.customer_tbl),
    path('product/', views.product_tbl),
    path('order/',views.order_tbl),

]