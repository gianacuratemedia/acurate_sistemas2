from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, BaseUserManager

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _




#MODELO SUPERUSUARIO
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Los usuarios deben tener un nombre de usuario')
        if email is None:
            raise TypeError('Los usuarios deben tener un email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Debes ingresar una contraseña')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

AUTH_PROVIDERS = {'email': 'email'}
#MODELO CUSTOMUSER


class CustomUser(AbstractUser):
    
    fecha_nacimiento=models.DateField(blank=True, null=True)
    username= models.CharField(null=False, max_length=50, unique=True)
    biografia=models.TextField(blank=True)
    email = models.EmailField(_('direccion de email'), unique=True)
    telefono=models.CharField(null=True, max_length=12)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password=models.CharField(null=False, max_length=40)
    direccion=models.CharField(null=True, max_length=100)
    ciudad= models.CharField(null=True, max_length=50)
    estado= models.CharField(null=True, max_length=80)
    pais=models.CharField(null=True, max_length=80)
    codigo_postal=models.CharField(null=True, max_length=80)
    aceptacion_terminos=models.BooleanField(null= False, default=0)
    codigo_verificacion=models.CharField(null= True, max_length=150)
    registro_id=models.IntegerField(null=True)
    nivel=models.IntegerField(null=False, default=0)
    fecha_registro=models.DateTimeField(auto_now_add=True)
    ultima_visita=models.DateTimeField(auto_now=True)
    dias_premium=models.IntegerField(null=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))
    def register(self):
        self.save()

@staticmethod
def get_customer_by_email(email):
        try:
            return CustomUser.objects.get(email=email)
        except:
            return False


def isExists(self):
        if CustomUser.objects.filter(email = self.email):
            return True

        return  False


def __str__(self):
        return self.email

def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        
