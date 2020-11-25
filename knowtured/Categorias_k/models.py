from django.db import models
from Usuarios_k.models import User


# Create your models here.


class Categoria(models.Model):

    nombre= models.CharField(null=True, max_length=150)
    descripcion=models.TextField(blank=True)
    img_categoria=models.ImageField(null=True, upload_to='images/categorias/')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.owner)+'s category'
