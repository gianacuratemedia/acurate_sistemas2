from rest_framework import serializers
from .models import Realiza


class RealizaSerializer(serializers.ModelSerializer):

   class Meta:
       model = Realiza
       fields = ('pk','usuario_id', 'contenido_id','fecha_hora', 'calificacion','archivo')