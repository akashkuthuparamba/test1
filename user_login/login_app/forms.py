from dataclasses import field, fields
from operator import mod
from pyexpat import model
from django.forms import ModelForm
from . models import Log_in



class Myform(ModelForm):
    
    class Meta:
        model = Log_in
        fields ="__all__"


class Loginform(ModelForm):
    class Meta:
        model=Log_in
        fields=['username','password']