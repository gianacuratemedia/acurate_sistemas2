from rest_framework import serializers, fields
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):
    fecha_hora = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    class Meta:
        model = Evento
        fields = ['id','nota','fecha_hora', 'nombre']