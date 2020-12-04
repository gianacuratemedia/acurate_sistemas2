from rest_framework import serializers
from .models import Califica


class CalificaSerializer(serializers.ModelSerializer):

   class Meta:
       model = Califica
       fields = ('id','usuario_tutor', 'calificacion')
