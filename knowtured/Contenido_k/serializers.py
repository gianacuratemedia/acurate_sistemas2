from rest_framework import serializers
from .models import Contenido


class ContenidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contenido
        fields = ['id', 'curso_id', 'tipo', 'mensaje','archivo','fecha_limite']


class PublicContenidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contenido
        fields = ['curso_id', 'tipo', 'mensaje','archivo','fecha_limite']
