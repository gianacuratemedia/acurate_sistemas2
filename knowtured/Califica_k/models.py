from django.db import models

from Usuarios_k.models import *
# Create your models here.
class Califica(models.Model):
     
     usuario_alumno = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="usuario_alumno") 
     usuario_tutor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="usuario_tutor") 
     calificacion=models.IntegerField()
fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)
			
def __str__(self):
		return self.calificacion