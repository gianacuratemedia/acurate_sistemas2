from rest_framework import serializers
from .models import Foro

#Para crear un mensaje en el foro de un curso
class ForoSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = ['id','curso_id','mensaje']

#Para visualizar los mensajes del foro de un curso 
class ForoSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = ['id','curso_id','owner','mensaje','created_at']


#Para actualizar un mensaje en el foro de un curso
class ForoSerializerUpdateMessage(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = ['id','mensaje']