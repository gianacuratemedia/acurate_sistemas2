from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import CursoSerializer, CursoSerializerP
from .models import Curso
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


class CursoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            curso = Curso.objects.get(id=id)
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso

    # Get un curso
    def get(self, request, id):

        curso = self.get_queryset(id)
        serializer = CursoSerializer(curso)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un curso
    def put(self, request, id):
        
        curso = self.get_queryset(id)

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
    def delete(self, request, id):

        curso = self.get_queryset(id)

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
   

class CursoList(ListCreateAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Create un nuevo curso
    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#LISTA SIN PERMISO DE AUTENTIFICACIÓN

@permission_classes((AllowAny, ))
class CursoListP(ListAPIView):
       serializer_class = CursoSerializerP
       queryset = Curso.objects.all()
