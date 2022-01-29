from pyexpat import model
from django import forms
from .models import *

class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('__all__')
