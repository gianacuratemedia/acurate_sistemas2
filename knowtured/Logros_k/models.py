from django.db import models
from Usuarios_k.models import *

# Create your models here.
class Logro(models.Model):
     
     owner = models.ForeignKey(to=User, on_delete=models.CASCADE) 
     nombre= models.CharField(null=True, max_length=150)
     nivel_desbloqueo=models.IntegerField()
     descripcion= models.CharField(null=True, max_length=150)
     img_logro=models.ImageField(null=True, upload_to='images/logros/')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
        ordering: ['-updated_at']

     def __str__(self):
        return str(self.nombre)	
