from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Selecciona
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def selecciona_list(request):
    # GET lista de categorías, POST seguir una categoría nueva, DELETE una de las categorías seleccionadas
  if request.method == 'GET':
        seleccionas = Selecciona.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            seleccionas = seleccionas.filter(title__icontains=title)
        
        seleccionas_serializer = SeleccionaSerializer(seleccionas, many=True)
        return JsonResponse(seleccionas_serializer.data, safe=False)
       
  elif request.method == 'POST':
         
      selecciona_data = JSONParser().parse(request)
      selecciona_serializer = SeleccionaSerializer(data=selecciona_data)
      if selecciona_serializer.is_valid():
        selecciona_serializer.save()
        return JsonResponse(selecciona_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(selecciona_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
      elif request.method == 'DELETE':
        count = Selecciona.objects.all().delete()
        return JsonResponse({'message': '{} Las categorías a las que sigues han sido eliminadas'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def selecciona_detail(request, pk):
    # find selecciona by pk (id)
    try: 
        selecciona = Selecciona.objects.get(pk=pk) 
    except Selecciona.DoesNotExist: 
        return JsonResponse({'message': 'No sigue a la categoría seleccionada'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE selección

    if request.method == 'GET': 
         selecciona_serializer = SeleccionaSerializer(selecciona) 
         return JsonResponse(selecciona_serializer.data) 
        
    elif request.method == 'PUT': 
        selecciona_data = JSONParser().parse(request) 
        selecciona_serializer = SeleccionaSerializer(selecciona, data=selecciona_data) 
        if selecciona_serializer.is_valid(): 
            selecciona_serializer.save() 
            return JsonResponse(selecciona_serializer.data) 
        return JsonResponse(selecciona_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        selecciona.delete() 
        return JsonResponse({'message': 'Has eliminado la categoría a la que sigues'}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET'])
def selecciona_list_published(request):
     # GET todas las categorías que sigues
    seleccionas = Selecciona.objects.filter(published=True)
        
    if request.method == 'GET': 
        seleccionas_serializer = SeleccionaSerializer(seleccionas, many=True)
        return JsonResponse(seleccionas_serializer.data, safe=False)
         