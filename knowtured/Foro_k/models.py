from django.db import models
from Usuarios_k.models import User
from Curso_k.models import Curso
# Create your models here.
class Foro(models.Model):

   curso_id=models.ForeignKey(to=Curso, on_delete=models.CASCADE) 
   owner = models.ForeignKey(to=User, on_delete=models.CASCADE) 
   mensaje= models.CharField(null=True, max_length=150)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

class Meta:
        ordering: ['-created_at']

def __str__(self):
        return str(self.owner)+'s message'	
