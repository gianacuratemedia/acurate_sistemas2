from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SeleccionaSerializer
from .models import Selecciona
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

#Lista de categorias que sigue un usuario

class SeleccionaList(ListCreateAPIView):
    serializer_class = SeleccionaSerializer
    queryset = Selecciona.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Post selecciona una categoria
    def post(self, request):
        serializer = SeleccionaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeleccionaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SeleccionaSerializer

    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    
    def get_queryset(self,id):
        try:
            selecciona = Selecciona.objects.get(id=id)
        except Selecciona.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return selecciona

    # Get categoria que el alumno sigue por id
    def get(self, request, id):

        selecciona = self.get_queryset(id)
        serializer = SeleccionaSerializer(selecciona)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete dejar de seguir una categoria
    def delete(self, request, id):

        seleciona = self.get_queryset(id)

        if(request.user == seleciona.owner): # Si owner es quien hace el request
            seleciona.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   


         
