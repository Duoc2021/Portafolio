from typing import ClassVar
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save
import uuid

# Create your models here.


class Direccion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

opciones_estado = [
    [0, "MANTENCION"],
    [1, "DISPONIBLE"],
    [2, "OCUPADO"]
]

class Departamento(models.Model): 
    nombre = models.CharField(max_length=50)
    ubicacion= models.CharField(max_length=60)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="departamento", null=True)
    imagen2 = models.ImageField(upload_to="departamento", null=True)
    imagen3 = models.ImageField(upload_to="departamento", null=True)
    estado = models.IntegerField(choices=opciones_estado)

    def __str__(self):
        return self.nombre


opciones_consultas = [
    [0, "CONSULTAS"],
    [1, "RECLAMOS"],
    [2, "SUGERENCIAS"],
    [3, "FELICITACIONES"]
  
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_registro = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre


class Tour(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion_partida= models.CharField(max_length=60)
    descripcion = models.TextField()
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="tour", null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


tipo_trabajador = [
    [1, "Administrador"],
    [2, "Guardia"],
    [3, "Recepcionista"],
    [4, "Limpieza"]
]

sexo = [
    [1, "Mujer"],
    [2, "Hombre"],
    [3, "No definido"]
]


class Trabajador(models.Model): 
    tipo_trabajador = models.IntegerField(choices=tipo_trabajador)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    telefono = models.IntegerField(max_length=10)
    sexo = models.IntegerField(choices=sexo)
    pago = models.IntegerField(default=0)
    correo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

tipo_proveedor = [
    [1, "Transporte"],
    [2, "Alimento"],
    [3, "Mantencion"],
]


class Proveedor(models.Model): 
    tipo_proveedor = models.IntegerField(choices=tipo_proveedor)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=10)
    pago = models.IntegerField(default=0)
    correo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

tipo_estado = [
    [1, "Pagado"],
    [2, "No pagado"],
    [3, "Cancelado"]
]

class Reserva(models.Model):
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    cant_dias = models.SmallIntegerField('Cantidad de dias a reservar')
    estado = models.IntegerField(default=1, choices=tipo_estado)
    

    class Meta:

        verbose_name = 'Reserva'
        verbose_name_plural =   'Reservas'

    def __str__(self):
        return f'Reserva de Departamento {self.departamento}'


class Cliente(User):

    class Meta:
        proxy = True

    def get_departamentos(self):
        return[]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    biografia = models.TextField()

class Carrito(models.Model):
    carro_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    departamento = models.ManyToManyField(Departamento)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carro_id

def set_carro_id(sender, instance,*args,**kwargs):
        if not instance.carro_id:
         instance.carro_id = str(uuid.uuid4())

pre_save.connect(set_carro_id, sender=Carrito)