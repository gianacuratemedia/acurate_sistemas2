from rest_framework import serializers
from .models import Logro


class LogroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logro
        fields = ['id', 'nombre','nivel_desbloqueo', 'descripcion','img_logro']