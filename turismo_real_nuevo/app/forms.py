from django import forms
from django.forms import widgets
from .models import Contacto, Departamento, Tour, Trabajador, Proveedor, Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_registro", "mensaje", "avisos"]

        #fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


class DepartamentoForm(forms.ModelForm):  
    class Meta:  
        model = Departamento 
        fields = '__all__' 


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        #fields = ["departamento", "nombre", "correo", "cant_dias", "fecha_creacion", "estado", "fecha_llegada"]
    