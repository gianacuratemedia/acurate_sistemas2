from django.db import models
from Usuarios_k.models import *

# Create your models here.
class Curso(models.Model):
     
     usuario_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Tiempo de registro',auto_now_add=True)
     nombre=models.CharField(max_length=100, null=False)
     img_portada_ubicacion=models.CharField('ubicación',max_length=100)
     img_extension=models.CharField('extension',max_length=10)
     premium=models.CharField(max_length=2,null=False)
     duracion=models.CharField(max_length=20,null=False)
     dificultad=models.CharField(max_length=50,null=False)
     limite=models.IntegerField(null=False)
     descripcion=models.CharField(max_length=300,null=False)

	
def __str__(self):
		return self.pk