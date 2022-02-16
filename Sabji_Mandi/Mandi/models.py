from django import db
from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(auto_created=True, primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    customer_picture = models.FileField(upload_to ='photos', blank=True)
    is_login = models.BooleanField(default=False, blank=True)

    class Meta:
        db_table = 'customer_tbl'

class Products(models.Model):
    product_id = models.AutoField(auto_created=True, primary_key=True)
    product_name = models.CharField(max_length=50, blank=True)
    product_price = models.CharField(max_length=50, blank=True)
    product_desc = models.CharField(max_length=50, blank=True)
    product_picture = models.ImageField(upload_to="products/", blank=True)

    class Meta:
        db_table = 'products_tbl'

class Contact(models.Model):
    contact_id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50,blank=True)
    phone_no = models.CharField(max_length=50, blank=True)
    message = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'contact_tbl'

class Order(models.Model):
    order_id = models.AutoField(auto_created=True, primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    Product_id = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True)
    address = models.CharField(max_length=50, blank=True)
    phone_no = models.CharField(max_length=50, blank=True)
    date = models.DateField()

    class Meta:
        db_table = 'order_tbl'

