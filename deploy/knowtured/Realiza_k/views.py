from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Realiza
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def realiza_list(request):
    # GET lista de tareas a realizar, POST subir una tarea, DELETE alguna tarea
  if request.method == 'GET':
        realizas = Realiza.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            realizas = realizas.filter(title__icontains=title)
        
        realizas_serializer = RealizaSerializer(realizas, many=True)
        return JsonResponse(realizas_serializer.data, safe=False)
       
  elif request.method == 'POST':
         
      realiza_data = JSONParser().parse(request)
      realiza_serializer = RealizaSerializer(data=realiza_data)
      if realiza_serializer.is_valid():
        realiza_serializer.save()
        return JsonResponse(realiza_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(realiza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
      elif request.method == 'DELETE':
        count = Realiza.objects.all().delete()
        return JsonResponse({'message': '{} Todos los registros han sido eliminados'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def realiza_detail(request, pk):
    # find realiza by pk (id)
    try: 
        realiza = Realiza.objects.get(pk=pk) 
    except Realiza.DoesNotExist: 
        return JsonResponse({'message': 'Registro de tarea y/o actividad no encontrado'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE realiza
    
        
@api_view(['GET'])
def realiza_list_published(request):
     # GET todas las tareas que el usuario tiene
    realizas = Realiza.objects.filter(published=True)
        
    if request.method == 'GET': 
        realizas_serializer = RealizaSerializer(realizas, many=True)
        return JsonResponse(realizas_serializer.data, safe=False)