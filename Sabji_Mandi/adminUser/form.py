from django import forms
from .models import *

class AdminDbForm(forms.ModelForm):
    class Meta:
        model = AdminDb
        fields = ("__all__")
