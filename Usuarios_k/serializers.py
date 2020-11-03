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
