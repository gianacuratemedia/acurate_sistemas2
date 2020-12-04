from rest_framework import serializers
from .models import Realiza


class RealizaSerializer_alumno(serializers.ModelSerializer):

   class Meta:
       model = Realiza
       fields = ('id','contenido_id', 'fecha_hora','archivo')

class RealizaSerializer_tutor(serializers.ModelSerializer):

   class Meta:
       model = Realiza
       fields = ('id','contenido_id','fecha_hora','calificacion','archivo')