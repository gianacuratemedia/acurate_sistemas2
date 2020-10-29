from django.db import models
from Curso_k.models import *

# Create your models here.
class Contenido(models.Model):
     
     curso_id = models.ForeignKey(Curso,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True) 
     tipo=models.CharField(max_length=500, null=False)
     mensaje=models.CharField(max_length=500, null=False)
     archivo_ubc=models.CharField(max_length=500, null=False)
     extension=models.CharField(max_length=10, null=False)
     fecha_limite=models.DateField()
			
def __str__(self):
		return self.pk