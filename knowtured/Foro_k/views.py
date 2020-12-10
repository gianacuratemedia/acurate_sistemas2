from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ForoSerializer, ForoSerializerr, ComentarioSerializer, ComentarioSerializerr
from .models import Foro, Comentario
from Usuarios_k.models import User
from Curso_k.models import Curso
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

#Lista foro creado por usuario

class ForoList(ListAPIView):
    serializer_class = ForoSerializer
    queryset = Foro.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

#View Get and post Foro por parametro curso
class ForoList_Curso_GP(ListCreateAPIView):
    serializer_class = ForoSerializer
    queryset = Foro.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        curso_id=self.kwargs['curso_id']
        try:
            foro = Foro.objects.all().filter(curso_id=curso_id)
        except Foro.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return foro

    # Create un nuevo foro por parametro curso_id en la url
       
    def post(self, request, *args, **kwargs):
        curso_id= Curso.objects.get(id=self.kwargs['curso_id'])
        serializer = ForoSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save(owner=self.request.user, curso_id=curso_id)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Get y delete por parametro de id_foro y curso_id en url
class ForoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ForoSerializerGet
 
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    #Obtener mensajes del foro por curso_id
    def get_queryset(self,id,curso_id):
        try:
            foro = Foro.objects.get(id=id,curso_id=curso_id)
        except Foro.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return foro

    # Get foro por id y curso_id
    def get(self, request, id, curso_id):

        foro = self.get_queryset(id, curso_id)
        serializer = ForoSerializerr(foro)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # Delete foro por id y curso_id
    def delete(self, request, id, curso_id):

        foro = self.get_queryset(id, curso_id)

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

#Lista de publicaciones hechas por el usuario

class ComentarioList(ListAPIView):
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)



#View Get and post Comentario por parametro id_curso e id_foro 
class ComentarioList_Curso_Foro_GP(ListCreateAPIView):
    serializer_class = ComentarioSerializer
    queryset = Comentario.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        foro_id=self.kwargs['foro_id']
        try:
            comentario = Comentario.objects.all().filter(foro_id=foro_id)
        except Foro.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return comentario

    # Create un nuevo comentario por parametro foro_id en la url
       
    def post(self, request, *args, **kwargs):
        foro_id= Foro.objects.get(id=self.kwargs['foro_id'])
        #username_u=request.user.username
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save(owner=self.request.user, foro_id=foro_id, username=self.request.user.username)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Get y delete por parametro de foro_id e id_mensaje en url
class ComentarioDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ForoSerializerGet
 
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    #Obtener mensajes por foro_id e id del mensaje 
    def get_queryset(self,id,foro_id):
        try:
            comentario = Comentario.objects.get(id=id,foro_id=foro_id)
        except Comentario.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return comentario

    # Get comentario por id y foro_id
    def get(self, request, id, foro_id):

        comentario = self.get_queryset(id, foro_id)
        serializer = ComentarioSerializerr(comentario)
        return Response(serializer.data, status=status.HTTP_200_OK)

 # Update un comentario por id y foro_id
    def put(self, request, id, foro_id):
        
        comentario = self.get_queryset(id, foro_id)

        if(request.user == comentario.owner): # Si el creador del comentario en quien hace el request
            #Update solo puede editarse el field mensaje 
            serializer = ComentarioSerializer(comentario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)



    # Delete comentario por id y comentario
    def delete(self, request, id, comentario_id):

        comentario = self.get_queryset(id,comentario_id)

        if(request.user == comentario.owner): # Si el creador es quien hace el request
            comentario.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   
