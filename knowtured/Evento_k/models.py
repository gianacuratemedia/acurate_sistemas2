from django.db import models
from Usuarios_k.models import *
# Create your models here.
class Evento(models.Model):
     
     usuario_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
     nota=models.CharField(max_length=500, null=False)
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)
     nombre=models.CharField(max_length=300, null=False)
			
def __str__(self):
		return self.nombre