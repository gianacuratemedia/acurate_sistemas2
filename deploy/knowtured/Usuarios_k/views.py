from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.contrib.sites.shortcuts import get_current_site
from .models import CustomUser
from .serializers import *
from django.contrib import messages
from django.core.mail import EmailMessage
from rest_framework.decorators import api_view
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.urls import reverse
from .utils import account_activation_token


@api_view(['POST'])
def register_user(request):

      customUser_data = JSONParser().parse(request)
      customUser_serializer = CustomUserSerializer(data=customUser_data)
     
      if customUser_serializer.is_valid():
        customUser_serializer.is_active = False
        customUser_serializer.save()

  
        email = CustomUser.objects.get(email=customUser_data['email'])

        current_site = get_current_site(request)
        email_body = {
                    'user': CustomUser.nombre_usuario,
                    'domain': current_site.domain,
                    'id': urlsafe_base64_encode(force_bytes(CustomUser.pk)),
                    'token': account_activation_token.make_token(CustomUser.token),
                }

        link = reverse('activate', kwargs={
                               'id': email_body['uid'], 'token': email_body['token']})

        email_subject = 'Activa tu cuenta'

        activate_url = 'http://'+current_site.domain+link

        email = EmailMessage(
        email_subject,
        'Hola'+CustomUser.nombre_usuario + ', Por favor, sigue el enlace a continuación para activar tu cuenta \n'+activate_url,
                    'noreply@jgj.com',
                    [email],
        )
        email.send(fail_silently=False)
        messages.success(request, 'La cuenta ha sido creda')
        return render(request, 'authentication/register.html')
        return JsonResponse(customUser_data, status=status.HTTP_201_CREATED)

