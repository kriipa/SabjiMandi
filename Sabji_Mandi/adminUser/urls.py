
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.home, name="homeAdmin"),
    path('customer/', views.customer_tbl),
    path('product/', views.product_tbl),
    path('order/', views.order_tbl),
    path('productform/', views.product_tbl),
    path('addproduct/', views.add_product, name="addproduct"),
    path('delete/<p_id>', views.delete_product, name="deleteproduct"),
    path('edit/<p_id>', views.edit_product, name="editproduct"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout),
    path('myweb/', views.mywebsite, name="mysite"),
    path('adduser/', views.addcustomer, name="adduser"),
    path('deleteorder/<order_id>', views.delete, name="orderid"),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
