from django.db import models

from Usuarios_k.models import *
# Create your models here.
class Califica(models.Model):
     
     usuario_alumno = models.ForeignKey(to=User,on_delete=models.CASCADE) 
     usuario_tutor = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='%(class)s_user_tutor') 
     calificacion=models.IntegerField(null=True)
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)

def __str__(self):
        return str(self.calificacion)
			
def save(self, *args, **kwargs):
        # Revisar campos duplicados
        try:
            califica = Califica.objects.get(usuario_alumno=self.usuario_alumno, usuario_tutor=self.usuario_tutor)
            raise NotImplementedError('Registros duplicados', code='invalid')
        except self.DoesNotExist:
            super().save(*args, **kwargs)

        # Campos duplicados inversos
        try:
            califica_new = Califica.objects.get(usuario_tutor=self.usuario_alumno, usuario_alumno=self.usuario_tutor)
            raise NotImplementedError('Registros duplicados', code='invalid')
        except self.DoesNotExist:
            super().save(*args, **kwargs)
