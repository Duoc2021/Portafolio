from django.test import TestCase
#from django.test import Departamento
from .views import Departamento
from app.models import Departamento


#@pytest.mark.django_db
#class CreateTest(TestCase):
#    def test_departamento(self):    
#    Departamento.objects.departamento(nombre='rodolfo')

class CreateTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Departamento.objects.create(name='Big')

    def test_first_name_label(self):
        departamento=Departamento.objects.get(id=1)
        name = author._meta.get_field('nombre').verbose_name
        self.assertEquals(name,'nombre')



