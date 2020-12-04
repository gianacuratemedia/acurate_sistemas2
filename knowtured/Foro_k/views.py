from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ForoSerializerPost, ForoSerializerGet, ForoSerializerUpdateMessage
from .models import Foro
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

#Lista de mensajes en el foro, solo por usuario

class ForoList(ListCreateAPIView):
    serializer_class = ForoSerializerPost
    queryset = Foro.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Post un mensaje
    def post(self, request):
        serializer = ForoSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ForoSerializerGet
 
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    #Obtener mensajes del foro por curso_id
    def get_queryset(self,curso_id):
        try:
            foro = Foro.objects.get(curso_id=curso_id)
        except Foro.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return foro

    # Get mensaje o publicacion por id
    def get(self, request, id):

        foro = self.get_queryset(id)
        serializer = ForoSerializerGet(foro)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update mensaje o publicacion por id
    def put(self, request, id):
        
        foro = self.get_queryset(id)

    # Si el quién publicó el mensaje en el foro es quien hace el request 
        if(request.user == foro.owner): 
            #Solo actualiza el mensaje
            serializer = ForoSerializerUpdateMessage(foro, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un mensaje o publicacion
    def delete(self, request, id):

        foro = self.get_queryset(id)

        if(request.user == foro.owner): # Si el creador es quien hace el request
            foro.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   
