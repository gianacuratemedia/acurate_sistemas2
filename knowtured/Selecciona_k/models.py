from django.db import models
from Usuarios_k.models import *
from Categorias_k.models import *
# Create your models here.
class Selecciona(models.Model):
     
     usuario = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
     categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)


def save(self, *args, **kwargs):
        # Revisar campos duplicados
        try:
            selecciona = Selecciona.objects.get(usuario=self.usuario, categoria=self.categoria)
            raise NotImplementedError('Registros duplicados', code='invalid')
        except self.DoesNotExist:
            super().save(*args, **kwargs)
     

def __str__(self):
		return self.categoria