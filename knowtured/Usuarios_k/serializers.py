


from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser
#from validate_email import validate_email
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


# Django
from django.contrib.auth import password_validation, authenticate

#Registrar usuario
"""class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=55, min_length=8)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(max_length=55, min_length=8)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        customUser = CustomUser.objects.create_user(validated_data['username'],validated_data['email'],
             validated_data['password'])
        return customUser"""
#REGISTRO DE USUARIO
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'El nombre de usuario solo debe contener caracteres alfanuméricos'}

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    #Verificacion de cuenta:
class EmailVerificationSerializer(serializers.ModelSerializer):
        token = serializers.CharField(max_length=555)
        class Meta:
          model = CustomUser
        fields = ['token']

#Login
class LoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        customuser = CustomUser.objects.get(email=obj['email'])

        return {
            'refresh': customuser.tokens()['refresh'],
            'access': customuser.tokens()['access']
        }

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email','')
        password = attrs.get('password','')
        filtered_user_by_email = CustomUser.objects.filter(email=email)

        customuser = authenticate(email=email, password=password)

        if not customuser:
            raise AuthenticationFailed('Error de email/contraseña, intentalo de nuevo')
        if not customuser.is_active:
            raise AuthenticationFailed('Cuenta inhabilitada')
        if not customuser.is_verified:
            raise AuthenticationFailed('Email no verificado')
        return {
            'email': customuser.email,
            'username': customuser.username,
            'tokens': customuser.tokens
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
