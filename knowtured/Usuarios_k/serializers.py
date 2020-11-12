from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser
from validate_email import validate_email
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

#Registrar usuario
class CustomUserSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(max_lemin_length=6)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all()), validate_email]
            )
    password = serializers.CharField(max_lemin_length=6)

    class Meta:
        model = CustomUser
        fields = ('pk','nombre_usuario', 'email', 'password')

    def create(self, validated_data):
        customUser = CustomUser.objects.create_user(validated_data['nombre_usuario'],validated_data['email'],
             validated_data['password'])
        return customUser

    #Verificacion de cuenta:
class EmailVerificationSerializer(serializers.ModelSerializer):
        token = serializers.CharField(max_length=555)
        class Meta:
          model = CustomUser
        fields = ['token']

#Login
class LoginSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        customUser = CustomUser.objects.get(email=obj['email'])

        return {
            'refresh': customUser.tokens()['refresh'],
            'access': customUser.tokens()['access']
        }

    class Meta:
        model = CustomUser
        fields = ['nombre_usuario','email', 'password', 'tokens']

    def validate(self, attrs):
         email = attrs.get('email', '')
         password = attrs.get('password', '')
         filtered_user_by_email = CustomUser.objects.filter(email=email)
         customUser = auth.authenticate(email=email, password=password)

         if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Continúe con su inicio de sesión usando ' + filtered_user_by_email[0].auth_provider)

         if not customUser:
            raise AuthenticationFailed('Credenciales inválidas, intentelo de nuevo')
         if not customUser.is_active:
            raise AuthenticationFailed('Cuenta inhabilitada, contacta con el administrador')
         if not customUser.is_verified:
            raise AuthenticationFailed('Email no verificado')

         return {
            'email': customUser.email,
            'nombre_usuario': customUser.nombre_usuario,
            'tokens': customUser.tokens
        }
      
        
         return super().validate(attrs)
         
#Cerrar sesión

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('El token ha expirado o es inválido')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


# Cambiar password
class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


#Login
class LoginSerializer(serializers.ModelSerializer):
    nombre_usuario = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        customUser = CustomUser.objects.get(email=obj['email'])

        return {
            'refresh': customUser.tokens()['refresh'],
            'access': customUser.tokens()['access']
        }

    class Meta:
        model = CustomUser
        fields = ['nombre_usuario','email', 'password', 'tokens']



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('El token ha expirado o es inválido')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
