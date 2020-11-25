from rest_framework import serializers
from .models import Curso


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['id', 'categoria_id','nombre', 'img_curso', 'premium', 'duracion','dificultad','limite','descripcion']


class CursoSerializerP(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['nombre', 'img_curso', 'premium', 'duracion','dificultad','limite','descripcion']
