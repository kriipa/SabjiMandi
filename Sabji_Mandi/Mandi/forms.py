from dataclasses import fields
from django import forms
from .models import *

class Customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("__all__")

class Product_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = ("__all__")

class Order_form(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("__all__")

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("__all__")
