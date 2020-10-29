from django.db import models
from Usuarios_k.models import *
from django.core.exceptions import ValidationError

# Create your models here.
class Sigue(models.Model):
         
     usuario_alumno = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="usuario_alumno") 
     usuario_tutor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="usuario_tutor") 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)
			
     def save(self, *args, **kwargs):
        # Revisar campos duplicados
        try:
            sigue = Sigue.objects.get(usuario_alumno=self.usuario_alumno, usuario_tutor=self.usuario_tutor)
            raise NotImplementedError('Registros duplicados', code='invalid')
        except self.DoesNotExist:
            super().save(*args, **kwargs)

        # Campos duplicados inversos
        try:
            sigue_new = Sigue.objects.get(usuario_tutor=self.usuario_alumno, usuario_alumno=self.usuario_tutor)
            raise NotImplementedError('Registros duplicados', code='invalid')
        except self.DoesNotExist:
            super().save(*args, **kwargs)
def __str__(self):
		return self.usuario_alumno