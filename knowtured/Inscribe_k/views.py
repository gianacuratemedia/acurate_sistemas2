from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import InscripcionSerializer
from .models import Inscripcion
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


# Create your views here.
class InscripcionView(ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Inscripcion.objects.all()

    def get_queryset(self):
        return self.queryset.filter(alumno_id=self.request.user)

    def post(self, request):
        serializer = InscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(alumno_id=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscripcionDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = InscripcionSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            inscripcion = Inscripcion.objects.get(id=id)
        except Inscripcion.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return inscripcion

    # Get una inscripcion
    def get(self, request, id):

        inscripcion = self.get_queryset(id)
        serializer = InscripcionSerializer(inscripcion)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete una inscripcion
    def delete(self, request, id):

        inscripcion = self.get_queryset(id)
        

        if(request.user == inscripcion.alumno_id): # If student is who makes request
            inscripcion.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   
