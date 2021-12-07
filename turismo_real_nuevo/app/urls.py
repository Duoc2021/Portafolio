from django.urls import path, include
from .views import home, contacto, quienes_somos, departamento, tour, registro, agregar_tour, modificar_tour, listar_tour, eliminar_tour,crear_departamento, listar_departamento, modificar_departamento, eliminar_departamento,listar_trabajador,modificar_trabajador,eliminar_trabajador,agregar_trabajador
from .views import add,agregar_proveedor,eliminar_proveedor,modificar_proveedor,listar_proveedor, carro,DepartamentoViewset, TourViewset, DireccionViewset,agregar_reserva,eliminar_reserva,listar_reserva,modificar_reserva
from rest_framework import routers


# localhost:8000/api/departamento
router = routers.DefaultRouter()
router.register('departamento', DepartamentoViewset),
router.register('tour', TourViewset),
router.register('direccion', DireccionViewset)

urlpatterns = [
    path('', home, name="home"),
    path('departamento/', departamento, name="departamento"),
    path('contacto/', contacto, name="contacto"),
    path('quienes-somos/', quienes_somos, name="quienessomos"),
    #path('galeria/', galeria, name="galeria"),    
    path('tour/', tour, name="tour"),    
    path('registro/', registro, name="registro"),
    path('agregar-tour/', agregar_tour, name="agregar_tour"),
    path('listar-tour/', listar_tour, name="listar_tour"),
    path('modificar-tour/<id>/', modificar_tour, name="modificar_tour"),
    path('eliminar-tour/<id>/', eliminar_tour, name="eliminar_tour"),
    path('crear-departamento/', crear_departamento, name="crear_departamento"),
    path('listar-departamento/', listar_departamento, name="listar_departamento"),
    path('modificar-departamento/<id>/', modificar_departamento, name="modificar_departamento"),
    path('eliminar-departamento/<id>/', eliminar_departamento, name="eliminar_departamento"),
    path('listar-trabajador/', listar_trabajador, name="listar_trabajador"),
    path('modificar-trabajador/<id>/', modificar_trabajador, name="modificar_trabajador"),
    path('agregar-trabajador/', agregar_trabajador, name="agregar_trabajador"),
    path('eliminar-trabajador/<id>/', eliminar_trabajador, name="eliminar_trabajador"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    path('agregar-proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('listar-proveedor/', listar_proveedor, name="listar_proveedor"),
    path('api/', include(router.urls)),
    path('agregar-reserva/', agregar_reserva, name="agregar_reserva"),
    path('eliminar-reserva/<id>/', eliminar_reserva, name="eliminar_reserva"),
    path('listar-reserva/', listar_reserva, name="listar_reserva"),
    path('modificar-reserva/<id>/', modificar_reserva, name="modificar_reserva"),
    path('carro/', carro, name="carro"),
    path('add/', add, name="add"),
]

