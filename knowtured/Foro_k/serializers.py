from rest_framework import serializers
from .models import Foro, Comentario

#Para crear un foro de un curso
class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = ['id', 'nombre']

#Get and delete by id and curso_id
class ForoSerializerr(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = ['id','curso_id', 'nombre']



#Para crear un comentario de un foro
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'mensaje']


#Para crear un comentario de un foro
class ComentarioSerializerr(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'mensaje','username','created_at']
