from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reporte


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2'] 


"""
** Models **
``NuevoReporteForm``
    A form that inherits from the Django ModelForm to create
    a new report.
"""


class NuevoReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['contenido', 'lugar']