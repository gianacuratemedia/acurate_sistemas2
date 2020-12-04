from rest_framework import serializers
from .models import Sigue


class SigueSerializer(serializers.ModelSerializer):

   class Meta:
       model = Sigue
       fields = ('id','usuario_tutor')