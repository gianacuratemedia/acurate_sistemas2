from django.db import models
from Usuarios_k.models import *
from Categorias_k. models import *


# Create your models here.
class Curso(models.Model):
     
     owner = models.ForeignKey(to=User,on_delete=models.CASCADE) 
     categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)
     nombre=models.CharField(max_length=100, null=False)
     img_curso=models.ImageField(null=True, upload_to='images/cursos/')
     premium=models.CharField(max_length=2,null=False)
     duracion=models.CharField(max_length=50,null=False)
     dificultad=models.CharField(max_length=50,null=False)
     limite=models.IntegerField(null=True)
     descripcion=models.CharField(max_length=300,null=False)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
        ordering: ['-updated_at']

     def __str__(self):
        return str(self.owner)+'s course'
