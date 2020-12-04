from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializers import CalificaSerializer
from .models import Califica
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


# Create your views here.
class CalificaList(ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Califica.objects.all()

    def get_queryset(self):
        return self.queryset.filter(usuario_alumno=self.request.user)

    def post(self, request):
        serializer = CalificaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario_alumno=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalificaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CalificaSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            califica = Califica.objects.get(id=id)
        except Califica.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return califica

    # Get califica
    def get(self, request, id):

        califica = self.get_queryset(id)
        serializer = CalificaSerializer(califica)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete una calificacion
    def delete(self, request, id):

        califica = self.get_queryset(id)
        

        if(request.user == califica.usuario_alumno): # If student is who makes request
            califica.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   
