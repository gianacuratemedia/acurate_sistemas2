from django.db import models
from Usuarios_k.models import *
from Curso_k.models import *

# Create your models here.
class Inscribe(models.Model):
     
     usuario_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
     curso_id = models.ForeignKey(Curso,on_delete=models.CASCADE) 
     fecha_inscripcion=models.DateTimeField('Fecha de inscripción:',auto_now_add=True)
     promedio=models.DecimalField(null=True)
    

	
def __str__(self):
		return self.curso_id