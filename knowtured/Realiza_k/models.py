from django.db import models
from Usuarios_k.models import *
from Contenido_k.models import *
# Create your models here.

class Realiza(models.Model):
     
     usuario_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
     contenido_id = models.ForeignKey(Contenido,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)
     calificacion=models.DecimalField(null=True)
     archivo=models.FileField(upload_to='Recursos/Tareas', null=True, blank= True)

     def save(self, *args, **kwargs):
        # Revisar campos duplicados
        try:
            realiza = Realiza.objects.get(usuario_id=self.usuario_id, contenido_id=self.contenido_id)
            raise NotImplementedError('Registros duplicados', code='invalid')
        except self.DoesNotExist:
            super().save(*args, **kwargs)
			
def __str__(self):
		return self.contenido_id