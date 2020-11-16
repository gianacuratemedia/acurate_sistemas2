from rest_framework import serializers
from .models import Califica


class CalificaSerializer(serializers.ModelSerializer):

   class Meta:
       model = Califica
       fields = ('pk','usuario_alumno', 'usuario_tutor','calificacion')
