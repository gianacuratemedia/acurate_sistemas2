from django.db import models
from Usuarios_k.models import *


# Create your models here.
"""Modelo tabla Premium"""
class Premium(models.Model):
     
     usuario_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
     total= models.DecimalField(null=True)
     dias=models.IntegerField(null=True)
     fecha_hora=models.DateTimeField('Hora de registro',auto_now_add=True)
     no_tarjeta=models.IntegerField(null=False)
     fecha_expiracion=models.DateField(blank=True)
     codigo_seg=models.IntegerField(max_length=3)
     nombre=models.CharField(null= True, max_length=150)
     apellido_paterno=models.CharField(null= True, max_length=150)
     apellido_materno=models.CharField(null= True, max_length=150)
     direccion=models.CharField(null=True, max_length=100)
     ciudad= models.CharField(null=True, max_length=50)
     estado= models.CharField(null=True, max_length=80)
     pais=models.CharField(null=True, max_length=80)
     codigo_postal=models.CharField(null=True, max_length=80)
     rfc=models.CharField(null=True, max_length=13)
     tipo=models.CharField(null=True, max_length=20)
     email=models.EmailField(null= False)
     estado_compra= models.CharField(max_length=30, null=True)
	
def __str__(self):
		return self.usuario_id
