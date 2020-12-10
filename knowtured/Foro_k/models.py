rom django.db import models
from Usuarios_k.models import User
from Curso_k.models import Curso
# Create your models here.
class Foro(models.Model):

   curso_id=models.ForeignKey(to=Curso, on_delete=models.CASCADE) 
   owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
   nombre= models.CharField(null=True,max_length=50) 
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
        ordering: ['-created_at']

   def __str__(self):
        return str(self.owner)+'s foro'	

class Comentario(models.Model):

   foro_id=models.ForeignKey(to=Foro, on_delete=models.CASCADE) 
   owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
   username=models.CharField(max_length=200, null=False)
   mensaje=models.CharField(max_length=800, null=False) 
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
        ordering: ['-updated_at']

   def __str__(self):
        return str(self.owner)+'s comment'
