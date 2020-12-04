from django.db import models
from Usuarios_k.models import *
from Curso_k.models import Contenido
# Create your models here.

class Realiza(models.Model):
     
     alumno_id = models.ForeignKey(to=User,on_delete=models.CASCADE) 
     contenido_id = models.ForeignKey(to=Contenido,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)
     calificacion=models.FloatField(null=True)
     archivo=models.FileField(upload_to='Recursos/Tareas', null=True, blank= True)

     def save(self, *args, **kwargs):
        # Revisar campos duplicados
        try:
            realiza = Realiza.objects.get(alumno_id=self.alumno_id, contenido_id=self.contenido_id)
            raise NotImplementedError('Registros duplicados', code='invalid')
        except self.DoesNotExist:
            super().save(*args, **kwargs)
			
def __str__(self):
		return self.contenido_id
