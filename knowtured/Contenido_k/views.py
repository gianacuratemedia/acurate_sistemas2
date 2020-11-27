from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import ContenidoSerializer, PublicContenidoSerializer
from .models import Contenido
from Curso_k.models import Curso
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

class ContenidoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ContenidoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            contenido = Contenido.objects.get(id=id)
        except Contenido.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return contenido

    # Get una contenido
    def get(self, request, id):

        contenido = self.get_queryset(id)
        serializer = ContenidoSerializer(contenido)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un contenido
    def put(self, request, id):
        
        contenido = self.get_queryset(id)

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

    # Delete una categoria
    def delete(self, request, id):

        contenido = self.get_queryset(id)
        

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
        return self.queryset.filter(owner=self.request.user)

    # Create una nueva categoria
    def post(self, request):
       
        serializer = ContenidoSerializer(data=request.data)
        if(request.user ==Curso.owner):
          if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#LISTA SIN PERMISO DE AUTENTIFICACIÓN

@permission_classes((AllowAny, ))
class ContenidoListP(ListAPIView):
       serializer_class = PublicContenidoSerializer
       queryset = Contenido.objects.all().order_by('curso_id')
