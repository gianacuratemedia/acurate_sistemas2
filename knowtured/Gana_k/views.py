from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import GanaSerializer
from .models import Gana
from Usuarios_k.models import User
from Logros_k.models import Logro
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

#Lista de logros por usuario

class GanaList(ListCreateAPIView):
    serializer_class = GanaSerializer
    queryset = Gana.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Post 
    def post(self, request):
     serializer = GanaSerializer(data=request.data)
     if(request.user.nivel == Logro.nivel_desbloqueo): # Si el nivel del usuario es el mismo, asignar logro

           if serializer.is_valid():
              serializer.save(owner=self.request.user)
              return Response(serializer.data, status=status.HTTP_201_CREATED)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     else:
            content={
                'status':'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

class GanaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = GanaSerializer
 
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    
    def get_queryset(self,id):
        try:
            gana= Gana.objects.get(id=id)
        except Gana.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return gana

    # Get gana
    def get(self, request, id):

        gana = self.get_queryset(id)
        serializer = GanaSerializer(gana)
        return Response(serializer.data, status=status.HTTP_200_OK)
