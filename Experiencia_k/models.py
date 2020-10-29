from django.db import models
from Usuarios_k.models import *
# Create your models here.
class Experiencia(models.Model):
     
     usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
     nombre= models.CharField(null=True, max_length=150)
     fecha_creacion=models.DateTimeField("Fecha de registro",auto_now_add=True)
     fecha_inicio=models.DateField(blank=True, null=True)
     fecha_fin=models.DateField(blank=True, null=True)
	
def __str__(self):
		return self.nombre