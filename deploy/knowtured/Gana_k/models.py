from django.db import models
from Usuarios_k.models import *
from Logros_k.models import *
# Create your models here.
class Gana(models.Model):
     
     id_logro= models.ForeignKey(Logro, on_delete=models.CASCADE, related_name="id_logro") 
     usuario = models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)
			
def __str__(self):
		return self.id_logro