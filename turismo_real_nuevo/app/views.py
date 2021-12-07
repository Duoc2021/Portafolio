from django.contrib.auth.models import User, UserManager
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from .models import Carrito, Departamento, Direccion, Proveedor, Reserva, Tour, Trabajador
from .forms import ContactoForm, DepartamentoForm, CustomUserCreationForm, ProveedorForm, TourForm, TrabajadorForm, ProveedorForm,ReservaForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from rest_framework import viewsets
from .serializers import DepartamentoSerializer, TourSerializer, DireccionSerializer
from .funciones import funcionCarrito

# Create your views here.


class DireccionViewset(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class DepartamentoViewset(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    def get_queryset(self):
        departamentos = Departamento.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            departamentos= departamentos.filter(nombre__contains=nombre)

        return departamentos


class TourViewset(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_queryset(self):
        tours = Tour.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            tours= tours.filter(nombre__contains=nombre)

        return tours

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    data = {
        'form' : ContactoForm()
    }

    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "CONTACTO GUARDADO")

        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)

def quienes_somos(request):
    return render(request, 'app/quienessomos.html')

def departamento(request):
    departamento = Departamento.objects.all()
    data = {
        'departamento': departamento
    }
    return render(request, 'app/departamento.html', data)

def tour(request):
    tour = Tour.objects.all()
    data = {
        'tour': tour
    }
    return render(request, 'app/tour.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            #login(request, user)
            messages.success(request, "Registro Exitoso")
            return redirect(to="home")

        data["form"] = formulario
        
        

    return render(request, 'registration/registro.html', data)

# Creacion CRUD TOUR
@permission_required('app.add_tour')
def agregar_tour(request):

    data = {
        'form': TourForm()
    }

    if request.method == 'POST':
        formulario = TourForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Tour guardado exitosamente") 
            
        else:
            data["form"] = formulario

    return render(request, 'app/tour/agregar.html', data)

@permission_required('app.view_tour')
def listar_tour(request):
    tour = Tour.objects.all()

    data = {
        'tour': tour
    }
    return render(request, 'app/tour/listar.html', data)

@permission_required('app.change_tour')
def modificar_tour(request, id):

    tour = get_object_or_404(Tour, id=id)

    data = {
        'form': TourForm(instance=tour)
    }

    if request.method == 'POST':
        formulario = TourForm(data=request.POST, instance=tour, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Exitoso")
            return redirect(to="listar_tour")

        data["form"] = formulario

    return render(request, 'app/tour/modificar.html', data)

@permission_required('app.delete_tour')
def eliminar_tour(request, id):
    tour = get_object_or_404(Tour, id=id)
    tour.delete()
    messages.success(request, "Tour Eliminado Exitosamente")
    return redirect(to="listar_tour")
    



# Creacion CRUD DEPARTAMENTO

@permission_required('app.view_departamento')
def listar_departamento(request):
    
    departamentos = Departamento.objects.all()

    data = {
        'departamentos' : departamentos
    }

    return render(request, 'app/departamento/listar.html',data)

@permission_required('app.change_departamento')
def modificar_departamento(request, id):

    departamento = get_object_or_404(Departamento, id = id)

    data = {
        'form' : DepartamentoForm(instance=departamento)
    }

    if request.method == 'POST' :
        formulario = DepartamentoForm(data = request.POST, instance=departamento, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_departamento")
        data["form"] = formulario
    return render(request, 'app/departamento/modificar.html',data)

@permission_required('app.add_departamento') 
def crear_departamento(request):

    data = {
        'form': DepartamentoForm()
    }

    if request.method == 'POST':
        formulario = DepartamentoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Departamento guardado exitosamente") 
            #data["mensaje"] = "Departamento guardado exitosamente"
        else:
            data["form"] = formulario

    return render(request, 'app/departamento/crear.html', data)

@permission_required('app.delete_departamento')
def eliminar_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    departamento.delete()
    messages.success(request, "Departamento Eliminado Exitosamente")
    return redirect(to="listar_departamento")


# Creacion CRUD TRABAJADOR

@permission_required('app.view_trabajador')
def listar_trabajador(request):
    
    trabajadores = Trabajador.objects.all()

    data = {
        'trabajador' : trabajadores
    }

    return render(request, 'app/trabajador/listar.html',data)

@permission_required('app.change_trabajador')
def modificar_trabajador(request, id):

    trabajador = get_object_or_404(Trabajador, id = id)

    data = {
        'form' : TrabajadorForm(instance=trabajador)
    }

    if request.method == 'POST' :
        formulario = TrabajadorForm(data = request.POST, instance=trabajador, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_trabajador")
        data["form"] = formulario
    return render(request, 'app/trabajador/modificar.html',data)

@permission_required('app.add_trabajador')
def agregar_trabajador(request):

    data = {
        'form': TrabajadorForm()
    }

    if request.method == 'POST':
        formulario = TrabajadorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Trabajador guardado exitosamente") 
            #data["mensaje"] = "Trabajador guardado exitosamente"
        else:
            data["form"] = formulario

    return render(request, 'app/trabajador/agregar.html', data)

@permission_required('app.delete_trabajador')
def eliminar_trabajador(request, id):
    trabajador = get_object_or_404(Trabajador, id=id)
    trabajador.delete()
    messages.success(request, "Trabajador Eliminado Exitosamente")
    return redirect(to="listar_trabajador")




    # Creacion CRUD PROVEEDOR

@permission_required('app.view_proveedor')
def listar_proveedor(request):
    
    proveedores = Proveedor.objects.all()

    data = {
        'proveedor' : proveedores
    }

    return render(request, 'app/proveedor/listar.html',data)

@permission_required('app.change_proveedor')
def modificar_proveedor(request, id):

    proveedor = get_object_or_404(Proveedor, id = id)

    data = {
        'form' : ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST' :
        formulario = ProveedorForm(data = request.POST, instance=proveedor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_proveedor")
        data["form"] = formulario
    return render(request, 'app/proveedor/modificar.html',data)

@permission_required('app.add_proveedor')
def agregar_proveedor(request):

    data = {
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor guardado exitosamente") 
            #data["mensaje"] = "Proveedor guardado exitosamente"
        else:
            data["form"] = formulario

    return render(request, 'app/proveedor/agregar.html', data)

@permission_required('app.delete_proveedor')
def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    messages.success(request, "Proveedor Eliminado Exitosamente")
    return redirect(to="listar_proveedor")



# Creacion CRUD RESERVA

@permission_required('app.view_reserva')
def listar_reserva(request):
    
    reservas = Reserva.objects.all()

    data = {
        'reserva' : reservas
    }

    return render(request, 'app/reserva/listar.html',data)

@permission_required('app.change_reserva')
def modificar_reserva(request, id):

    reserva = get_object_or_404(Reserva, id = id)

    data = {
        'form' : ReservaForm(instance=reserva)
    }
    if request.method == 'POST' :
        formulario = ReservaForm(data = request.POST, instance=reserva, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_reserva")
        data["form"] = formulario
    return render(request, 'app/reserva/modificar.html',data)

@permission_required('app.add_reserva')
def agregar_reserva(request):

    data = {
        'form': ReservaForm()
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Reserva guardada exitosamente") 
            #data["mensaje"] = "Reserva guardado exitosamente"
        else:
            data["form"] = formulario

    return render(request, 'app/reserva/agregar.html', data)

@permission_required('app.delete_reserva')
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    messages.success(request, "Reserva Cancelada Exitosamente")
    return redirect(to="listar_reserva")



def carro(request):
  
    carro = funcionCarrito(request)

    return render(request,'app/carro.html',{})


def add(request):
    carro = funcionCarrito(request)
    departamento = Departamento.objects.get(pk=request.POST.get('departamento_id'))

    carro.departamentos.add(departamento)

    return render(request, 'app/add.html',{
        'departamento':departamento
    })