from django.db import models
from Usuarios_k.models import *
from Logros_k.models import *
# Create your models here.
class Gana(models.Model):
     
     id_logro= models.ForeignKey(to=Logro, on_delete=models.CASCADE, related_name="id_logro") 
     owner = models.ForeignKey(to=User,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
        ordering: ['-updated_at']

     def __str__(self):
        return str(self.owner)+'s logro'
