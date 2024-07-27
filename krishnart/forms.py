from django.db import models  
from django.forms import fields  
from .models import Drawings
from django import forms  
      
      
class Drawings(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Drawings
        # It includes all the fields of model  
        fields = ['name', 'caption', 'image']