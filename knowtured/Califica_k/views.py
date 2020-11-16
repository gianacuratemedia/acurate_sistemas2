from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Califica
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def califica_list(request):
    # GET lista de calificaciones, POST registrar calificación, DELETE una de las calificaciones
  if request.method == 'GET':
        calificas =Califica.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            calificas = calificas.filter(title__icontains=title)
        
        calificas_serializer = CalificaSerializer(calificas, many=True)
        return JsonResponse(calificas_serializer.data, safe=False)
       
  elif request.method == 'POST':
         
      califica_data = JSONParser().parse(request)
      califica_serializer = CalificaSerializer(data=califica_data)
      if califica_serializer.is_valid():
       califica_serializer.save()
      return JsonResponse(califica_serializer.data, status=status.HTTP_201_CREATED) 
      return JsonResponse(califica_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
  elif request.method == 'DELETE':
        count = Califica.objects.all().delete()
        return JsonResponse({'message': '{} Todas las calificaciones han sido eliminadas'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def califica_detail(request, pk):
    # find califica by pk (id)
     try: 
      califica = Califica.objects.get(pk=pk) 
     except Califica.DoesNotExist: 
      return JsonResponse({'message': 'La calificación seleccionada no existe'}, status=status.HTTP_404_NOT_FOUND) 
  
    # GET / PUT / DELETE califica

      if request.method == 'GET': 
         califica_serializer = CalificaSerializer(califica) 
         return JsonResponse(califica_serializer.data) 
        
      elif request.method == 'PUT': 
       califica_data = JSONParser().parse(request) 
       califica_serializer = CalificaSerializer(califica, data=califica_data) 
       if califica_serializer.is_valid(): 
        califica_serializer.save() 
        return JsonResponse(califica_serializer.data) 
        return JsonResponse(califica_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
      elif request.method == 'DELETE': 
        califica.delete() 
        return JsonResponse({'message': 'Has eliminado la calificación seleccionada'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def califica_list_published(request):
     # GET todas las calificaciones 
    calificas = Califica.objects.filter(published=True)
        
    if request.method == 'GET': 
        calificas_serializer = CalificaSerializer(calificas, many=True)
        return JsonResponse(calificas_serializer.data, safe=False)
