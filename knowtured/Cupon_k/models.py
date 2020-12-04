from django.db import models
from Usuarios_k.models import *
# Create your models here.
class Cupon(models.Model):
  owner= models.ForeignKey(to=User, on_delete=models.CASCADE) 
  cantidad_existencia=models.IntegerField()
  clave_promo= models.CharField(null=True, max_length=150)
  descuento=models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
   
  class Meta:
        ordering: ['-updated_at']

  def __str__(self):
        return str(self.clave_promo)
