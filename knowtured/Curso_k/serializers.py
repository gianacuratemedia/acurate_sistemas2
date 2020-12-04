from rest_framework import serializers
from .models import Curso, Contenido


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'categoria_id','nombre', 'img_curso', 'premium', 'duracion','dificultad','limite','descripcion']
    
    
class CursoSerializerP(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['nombre', 'img_curso', 'premium', 'duracion','dificultad','limite','descripcion']




class ContenidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contenido
        fields = ['id', 'curso_id', 'tipo', 'mensaje','archivo','fecha_limite']


class PublicContenidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contenido
        fields = ['curso_id', 'tipo', 'mensaje','archivo','fecha_limite']
