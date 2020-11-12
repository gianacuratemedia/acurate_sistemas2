from django.db import models
from Usuarios_k.models import *

# Create your models here.
class Logro(models.Model):
     
     usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
     fecha_creacion=models.DateTimeField("Fecha de creación",auto_now_add=True)
     nombre= models.CharField(null=True, max_length=150)
     nivel_desbloqueo=models.IntegerField()
     descripcion= models.CharField(null=True, max_length=150)
     img_ubicacion= models.CharField(null=True, max_length=500)
     img_extension= models.CharField(null=True, max_length=10)
	
def __str__(self):
		return self.nombre