from rest_framework import serializers
from .models import Categoria


class CategoriasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'img_categoria']
