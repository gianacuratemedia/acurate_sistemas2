from django.db import models
from Usuarios_k.models import *
# Create your models here.
class Evento(models.Model):
     
     owner = models.ForeignKey(to=User,on_delete=models.CASCADE) 
     nota=models.CharField(max_length=600, null=False)
     fecha_hora=models.DateField('Fecha y hora del evento',null=True)
     nombre=models.CharField(max_length=300, null=False)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
        ordering: ['-updated_at']

     def __str__(self):
        return str(self.owner)+'s event'	
