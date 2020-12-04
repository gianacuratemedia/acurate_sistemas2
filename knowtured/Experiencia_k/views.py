from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExperienciaSerializer
from .models import Experiencia
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

#Lista de experiencia, solo por usuario

class ExperienciaList(ListCreateAPIView):
    serializer_class = ExperienciaSerializer
    queryset = Experiencia.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Post experiencia 
    def post(self, request):
        serializer = ExperienciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExperienciaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienciaSerializer
 
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    
    def get_queryset(self,id):
        try:
            experiencia = Experiencia.objects.get(id=id)
        except Experiencia.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return experiencia

    # Get experiencia
    def get(self, request, id):

        experiencia = self.get_queryset(id)
        serializer = ExperienciaSerializer(experiencia)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update experiencia
    def put(self, request, id):
        
        experiencia = self.get_queryset(id)

        if(request.user == experiencia.owner): # Si el creador de la experiencia en quien hace el request
            serializer = ExperienciaSerializer(experiencia, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete experiencia
    def delete(self, request, id):

        experiencia = self.get_queryset(id)

        if(request.user == experiencia.owner): # Si el creador es quien hace el request
            experiencia.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   
