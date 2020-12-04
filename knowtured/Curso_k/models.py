from django.db import models
from Usuarios_k.models import *
from Categorias_k. models import *


# Create your models here.
class Curso(models.Model):
     owner = models.ForeignKey(to=User,on_delete=models.CASCADE) 
     categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)
     nombre=models.CharField(max_length=100, null=False)
     img_curso=models.ImageField(null=True,upload_to='images/cursos/')
     premium=models.CharField(max_length=2,null=False)
     duracion=models.CharField(max_length=50,null=False)
     dificultad=models.CharField(max_length=50,null=False)
     limite=models.IntegerField(null=True)
     descripcion=models.CharField(max_length=300,null=False)
     no_visitas=models.IntegerField(null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
        ordering: ['-updated_at']

     def __str__(self):
        return str(self.owner)+'s course'

# Create your models here.
class Contenido(models.Model):
     curso_id = models.ForeignKey(Curso,on_delete=models.CASCADE) 
     fecha_hora=models.DateTimeField('Registro de hora',auto_now_add=True) 
     tipo=models.CharField(max_length=500, null=False)
     mensaje=models.CharField(max_length=500, null=False)
     archivo_ubc=models.FileField(null=True, upload_to='cursos/contenido/')
     fecha_limite=models.DateField()
     owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
     no_vistas=models.IntegerField(null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     class Meta:
        ordering: ['-curso_id']

     def __str__(self):
        return str(self.owner)+'s contenido'
			
