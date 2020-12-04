from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import LogroSerializer
from .models import Logro
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


class LogroDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = LogroSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            logro = Logro.objects.get(id=id)
        except Logro.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return logro

    # Get un logro
    def get(self, request, id):

        logro = self.get_queryset(id)
        serializer = LogroSerializer(logro)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un logro
    def put(self, request, id):
        
        logro = self.get_queryset(id)

        if(request.user == logro.owner): # Si el creador del logro es quien hace el request
            serializer = LogroSerializer(logro, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un logro
    def delete(self, request, id):

        logro = self.get_queryset(id)

        if(request.user == logro.owner): # Si el creador es quien hace el request
            logro.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class LogroList(ListCreateAPIView):
    serializer_class = LogroSerializer
    queryset = Logro.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


    # Create un nuevo logro
    def post(self, request):
        serializer = LogroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



