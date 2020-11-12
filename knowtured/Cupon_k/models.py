from django.db import models
from Usuarios_k.models import *
# Create your models here.
class Cupon(models.Model):
     
     usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
fecha_creacion=models.DateTimeField("Fecha de registro",auto_now_add=True)
cantidad_existencia=models.IntegerField()
clave_promo= models.CharField(null=True, max_length=150)
descuento=models.DecimalField()

			
def __str__(self):
		return self.clave_promo