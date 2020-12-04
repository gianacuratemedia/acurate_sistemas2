from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import SigueSerializer
from .models import Sigue
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


# Create your views here.
class SigueList(ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Sigue.objects.all()
    def get_queryset(self):
        return self.queryset.filter(usuario_alumno=self.request.user)
    

    def post(self, request):
        serializer = SigueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(usuario_alumno=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigueDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SigueSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            sigue = Sigue.objects.get(id=id)
        except Sigue.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return sigue

    # Get sigue
    def get(self, request, id):

        sigue = self.get_queryset(id)
        serializer = SigueSerializer(sigue)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Delete un tutor
    def delete(self, request, id):

        sigue = self.get_queryset(id)
        

        if(request.user == sigue.usuario_alumno): # If student is who makes request
            sigue.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   
