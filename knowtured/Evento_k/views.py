from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import EventoSerializer
from .models import Evento
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes


class EventoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    
    def get_queryset(self,id):
        try:
            evento = Evento.objects.get(id=id)
            
            return self.queryset.filter(owner=self.request.user)
        except Evento.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return evento

    # Get un evento 
    def get(self, request, id):

        evento = self.get_queryset(id)
        serializer = EventoSerializer(evento)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un evento 
    def put(self, request, id):
        
        evento = self.get_queryset(id)

        if(request.user == evento.owner): # Si el creador del evento en quien hace el request
            serializer = EventoSerializer(evento, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un evento
    def delete(self, request, id):

        evento = self.get_queryset(id)

        if(request.user == evento.owner): # Si el creador es quien hace el request
            evento.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class EventoList(ListCreateAPIView):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Create un nuevo evento
    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
