from rest_framework import serializers
from .models import Inscripcion


class InscripcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inscripcion
        fields = ['id', 'curso_id','fecha_inscripcion', 'promedio']