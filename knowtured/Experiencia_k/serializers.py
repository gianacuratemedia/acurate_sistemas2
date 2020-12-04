from rest_framework import serializers, fields
from .models import Experiencia


class   ExperienciaSerializer(serializers.ModelSerializer):
    fecha_inicio = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    fecha_fin = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model = Experiencia
        fields = ['id','nombre','fecha_inicio','fecha_fin']