from django.db import models
from Usuarios_k.models import *
# Create your models here.
class Categoria(models.Model):
     
     usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
fecha_creacion=models.DateTimeField("Fecha de registro",auto_now_add=True)
nombre= models.CharField(null=True, max_length=150)
descripcion=models.TextField(blank=True)
img_categorias=models.CharField("Ruta de la imagen", null=True, max_length=150)
img_extension=models.CharField("Extensión de la imagen", null=True, max_length=150)
			
def __str__(self):
		return self.nombre