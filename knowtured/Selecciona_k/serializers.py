from rest_framework import serializers
from .models import Selecciona


class SeleccionaSerializer(serializers.ModelSerializer):

   class Meta:
       model = Selecciona
       fields = ('pk','categoria')
        