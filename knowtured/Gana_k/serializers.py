from rest_framework import serializers
from .models import Gana


class GanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gana
        fields = ['id','id_logro']