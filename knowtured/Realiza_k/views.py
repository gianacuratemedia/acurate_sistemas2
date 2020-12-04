from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RealizaSerializer_alumno, RealizaSerializer_tutor
from .models import Realiza
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

#Lista de las actividades realizadas, solo por usuario (alumno)

class RealizaList(ListCreateAPIView):
    serializer_class = RealizaSerializer_alumno
    queryset = Realiza.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(alumno_id=self.request.user)

    # Post realiza 
    def post(self, request):
        serializer = RealizaSerializer_alumno(data=request.data)
        if serializer.is_valid():
            serializer.save(alumno_id=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RealizaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = RealizaSerializer_alumno
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    
    def get_queryset(self,id):
        try:
            realiza = Realiza.objects.get(id=id)
        except Realiza.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return realiza

    # Get realiza
    def get(self, request, id):

        realiza = self.get_queryset(id)
        serializer = RealizaSerializer_alumno(realiza)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update realiza
    def put(self, request, id):
        
        realiza = self.get_queryset(id)

        if(request.user == realiza.alumno_id): # Si el alumno en quien hace el request
            serializer = RealizaSerializer_alumno(realiza, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete 
    def delete(self, request, id):

        realiza = self.get_queryset(id)

        if(request.user == realiza.alumno_id): # Si el alumno es quien hace el request
            realiza.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


#Tutor asignando calificacion
#Lista de calificaciones
class AsignarCalificaciones(ListCreateAPIView):
   serializer_class = RealizaSerializer_tutor
   permission_classes = (permissions.IsAuthenticated,)
   
   def get_queryset(self,contenido_id):
        try:
            realiza = Realiza.objects.get(contenido_id=contenido_id)
        except Realiza.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return realiza


class RealizaUpdateC(RetrieveUpdateDestroyAPIView):
    serializer_class = RealizaSerializer_tutor
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self,id):
        try:
            realiza = Realiza.objects.get(id=id)
        except Realiza.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return realiza

    # Get realiza
    def get(self, request, id):

        realiza = self.get_queryset(id)
        serializer = RealizaSerializer_tutor(realiza)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update realiza
    def put(self, request, id):
        
        realiza = self.get_queryset(id)
        serializer = RealizaSerializer_tutor(realiza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

