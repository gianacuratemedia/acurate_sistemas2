from rest_framework import serializers
from .models import Curso, Contenido, Contenido_Usuario


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'categoria_id','nombre', 'img_curso', 'premium', 'duracion','dificultad','limite','descripcion']

class CursoSerializerr(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id','nombre', 'img_curso', 'premium', 'duracion','dificultad','limite','descripcion']    

class CursoSerializerP(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['nombre', 'img_curso', 'premium', 'duracion','dificultad','limite','descripcion']




class ContenidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contenido
        fields = ['id','tipo', 'mensaje','archivo_ubc','fecha_limite']

class ContenidoSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Contenido
        fields = ['id','curso_id','tipo', 'mensaje','archivo_ubc','fecha_limite']


class PublicContenidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contenido
        fields = ['tipo', 'mensaje','archivo_ubc','fecha_limite']



class InfoCursoPay(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = ['nombre', 'owner','no_vistas','no_vistas_t']

class ShowIdCurso(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields=['owner']


class InfoContenidoPay(serializers.ModelSerializer):

    class Meta:
        model = Contenido_Usuario
        fields = ['owner','contenido_trimestral']


class ShowIdContenido(serializers.ModelSerializer):
    class Meta:
        model=Contenido_Usuario
        fields=['owner']
