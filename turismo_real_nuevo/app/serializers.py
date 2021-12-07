from .models import Departamento, Tour, Direccion
from rest_framework import serializers

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    nombre_direccion = serializers.CharField(read_only=True, source="direccion.nombre")
    direccion = DireccionSerializer(read_only=True)
    direccion_id = serializers.PrimaryKeyRelatedField(queryset=Direccion.objects.all(), source="direccion")
    nombre = serializers.CharField(required=True, min_length=3)

    def  validate_nombre(self, value):
        existe = Departamento.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Departamento ya Existe")

        return value

    class Meta:
        model = Departamento
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    nombre_direccion = serializers.CharField(read_only=True, source="direccion.nombre")
    direccion = DireccionSerializer(read_only=True)
    direccion_id = serializers.PrimaryKeyRelatedField(queryset=Direccion.objects.all(), source="direccion")
    nombre = serializers.CharField(required=True, min_length=3)

    def  validate_nombre(self, value):
        existe = Tour.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Tour ya Existe")

        return value
        
    class Meta:
        model = Tour
        fields = '__all__'