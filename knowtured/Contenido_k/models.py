from django.db import models
from Curso_k.models import *

# Create your models here.
class Contenido(models.Model):
     contenido_id = models.IntegerField(primary_key=True)
     curso_id = models.ForeignKey(Curso,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True) 
     tipo=models.CharField(max_length=500, null=False)
     mensaje=models.CharField(max_length=500, null=False)
     archivo_ubc=models.FileField(null=True, upload_to='cursos/contenido/')
     fecha_limite=models.DateField()
     owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
        ordering: ['-curso_id']

     def __str__(self):
        return str(self.owner)+'s contenido'
