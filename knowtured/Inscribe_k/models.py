from django.db import models
from Usuarios_k.models import *
from Curso_k.models import *

# Create your models here.
class Inscripcion(models.Model):
     curso_id = models.ForeignKey(Curso,on_delete=models.CASCADE)
     alumno_id = models.ForeignKey(to=User,on_delete=models.CASCADE)  
     fecha_inscripcion=models.DateTimeField('Fecha de inscripción:',auto_now_add=True)
     promedio=models.DecimalField(null=True, decimal_places=4, max_digits=10)
    

	
def __str__(self):
		return self.curso_id
