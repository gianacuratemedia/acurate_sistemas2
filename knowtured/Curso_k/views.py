from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import CursoSerializer, CursoSerializerP, ContenidoSerializer, PublicContenidoSerializer, CursoSerializerr
from .models import Curso, Contenido
from Categorias_k.models import Categoria
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


class CursoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id, categoria_id):
        try:
            curso = Curso.objects.get(id=id, categoria_id=categoria_id)
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso

    # Get un curso
    def get(self, request, id, categoria_id):

        curso = self.get_queryset(id, categoria_id)
        serializer = CursoSerializer(curso)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un curso
    def put(self, request, id, categoria_id):
        
        curso = self.get_queryset(id, categoria_id)

        if(request.user == curso.owner): # Si el creador del curso en quien hace el request
            serializer = CursoSerializer(curso, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un curso
    def delete(self, request, id, categoria_id):

        curso = self.get_queryset(id, categoria_id)

        if(request.user == curso.owner): # Si el creador es quien hace el request
            curso.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

#View Get and post Curso por parametro categoria 
class CursoList_Categoria_GP(ListCreateAPIView):
    serializer_class = CursoSerializerr
    queryset = Curso.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        categoria_id=self.kwargs['categoria_id']
        try:
            curso = Curso.objects.all().filter(categoria_id=categoria_id)
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso

    # Create un nuevo curso por categoria
       
    def post(self, request, *args, **kwargs):
        categoria_id= Categoria.objects.get(id=self.kwargs['categoria_id'])
        serializer = CursoSerializerr(data=request.data)
        if serializer.is_valid():
             serializer.save(owner=self.request.user, categoria_id=categoria_id)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#View todos los cursos creados por un usuario 
class CursoList(ListAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)





#Cursos por categoria_id
@permission_classes((AllowAny, ))
class Curso_Categoria_List(ListAPIView):

    def get_queryset(self, categoria_id):
        try:
            curso = Curso.objects.get(categoria_id=categoria_id)
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso


#LISTA SIN PERMISO DE AUTENTIFICACIÓN

@permission_classes((AllowAny, ))
class CursoListP(ListAPIView):
       serializer_class = CursoSerializerP
       queryset = Curso.objects.all()




#VIEWS CONTENIDO DE CURSO

class ContenidoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ContenidoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id, curso_id):
        try:
            contenido = Contenido.objects.get(id=id, curso_id=curso_id)
        except Contenido.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return contenido

    # Get un contenido
    def get(self, request, id, curso_id):

        contenido = self.get_queryset(id, curso_id)
        serializer = ContenidoSerializer(contenido)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un contenido
    def put(self, request, id, curso_id):
        
        contenido = self.get_queryset(id, curso_id)

        if(request.user == contenido.owner==Curso.owner): # If creator is who makes request
            serializer = ContenidoSerializer(contenido, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un contenido
    def delete(self, request, id, curso_id):

        contenido = self.get_queryset(id, curso_id)
        

        if(request.user == contenido.owner==Curso.owner): # If creator is who makes request
            contenido.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class ContenidoList(ListCreateAPIView):
    serializer_class = ContenidoSerializer
    queryset = Contenido.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        curso_id=self.kwargs['curso_id']
        try:
            contenido = Contenido.objects.all().filter(curso_id=curso_id)
        except Contenido.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return contenido

    # Create un nuevo contenido por curso
       
    def post(self, request, *args, **kwargs):
        curso_id= Curso.objects.get(id=self.kwargs['curso_id'])
        serializer = ContenidoSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save(owner=self.request.user, curso_id=curso_id)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#LISTA SIN PERMISO DE AUTENTIFICACIÓN

@permission_classes((AllowAny, ))
class ContenidoListP(ListAPIView):
       serializer_class = PublicContenidoSerializer
       queryset = Contenido.objects.all().order_by('curso_id')
