from django.db import models
from Usuarios_k.models import *
# Create your models here.
class Experiencia(models.Model):
     
   owner = models.ForeignKey(to=User, on_delete=models.CASCADE) 
   nombre= models.CharField(null=True, max_length=150)
   fecha_inicio=models.DateField(blank=True, null=True)
   fecha_fin=models.DateField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

class Meta:
        ordering: ['-updated_at']

def __str__(self):
        return str(self.owner)+'s experience'	
