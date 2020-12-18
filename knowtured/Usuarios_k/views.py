from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import RegisterSerializer, SetNewPasswordSerializer, ResetPasswordEmailRequestSerializer, EmailVerificationSerializer, LoginSerializer, LogoutSerializer
from .serializers import GetMyProfileSerializer, UpdateMyProfileSerializer, TeacherListSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from rest_framework.generics import ListAPIView, UpdateAPIView
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utils import Util
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
import os
from .permissions import IsOwner
from django.db.models import Q


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Hola '+user.username + \
            ', utiliza el siguiente link para verificar tu cuenta \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Verify your email'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Cuenta activada'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'La activación ha expirado'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      

class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hola, \n usa el siguiente link para restatablecer tu contraseña  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Restablece tu contraseña'}
            Util.send_email(data)
        return Response({'success': 'Te enviamos un link para restablecer tu contraseña'}, status=status.HTTP_200_OK)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Se ha restablecido la contraseña'}, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):   
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class PasswordTokenCheckAPI(generics.GenericAPIView):
    
   def get(self, request, uidb64, token):

      try:
          id=smart_str(urlsafe_base64_decode(uidb64))
          user=User.objects.get(id=id)
          if not PasswordResetTokenGenerator().check_token(user, token):
              return Response({'error':'Token no valido, por favor, solicita otro'},status=status.HTTP_401_UNAUTHORIZED )
          return Response({'sucess':'True, credenciales validas'},status=status.HTTP_200_OK)

      except DjangoUnicodeDecodeError as identifier:
             return Response({'error':'Token no valido, por favor, pide uno nuevo'},status=status.HTTP_401_UNAUTHORIZED )



#Get my profile
class MyProfile(ListAPIView):
    serializer_class = GetMyProfileSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

#Update my profile 
class MyProfileDetail(UpdateAPIView):
    serializer_class = UpdateMyProfileSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            profile = User.objects.get(id=id)
        except User.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return profile

    # Get my profile
    def get(self, request, id):

        profile = self.get_queryset(id)
        serializer = UpdateMyProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update my profile
    def put(self, request, id):
        
        profile = self.get_queryset(id)

        if(request.user.username == profile.username): # Si el perfil corresponde a quien hace el request
            serializer = UpdateMyProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

 
#Filtrar lista de usuarios por campo is_teacher

class ProfesoresList(ListAPIView):
    serializer_class = TeacherListSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(is_teacher=True)

#Barra de busqueda profesor por username, nombre o apellidos 

class BusquedaProfesor(ListAPIView):
    serializer_class = TeacherListSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self,*args, **kwargs):
        busqueda=self.kwargs['busqueda']
        try:
            user = User.objects.all().filter(
            Q(username__icontains=busqueda) 
            | Q(nombre__icontains=busqueda)
            | Q(apellido_paterno__icontains=busqueda)
            | Q(apellido_materno__icontains=busqueda)
            ).filter(is_teacher=True)
        except User.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return user



