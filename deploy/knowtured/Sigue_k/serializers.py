from rest_framework import serializers
from .models import Sigue


class SigueSerializer(serializers.ModelSerializer):

   class Meta:
       model = Sigue
       fields = ('pk','usuario_alumno', 'usuario_tutor','fecha_hora')