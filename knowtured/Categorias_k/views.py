from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Categoria
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def categoria_list(request):
    # GET lista de categorías, POST registrar una categoría nueva, DELETE una de las categorías seleccionadas
  if request.method == 'GET':
        categorias =Categoria.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            categorias = categorias.filter(title__icontains=title)
        
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(categorias_serializer.data, safe=False)
       
  elif request.method == 'POST':
         
      categoria_data = JSONParser().parse(request)
      categoria_serializer = CategoriaSerializer(data=categoria_data)
      if categoria_serializer.is_valid():
        categoria_serializer.save()
        return JsonResponse(categoria_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(categoria_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
      elif request.method == 'DELETE':
        count = Categoria.objects.all().delete()
        return JsonResponse({'message': '{} Todas las categorías han sido eliminadas'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk):
    # find categoria by pk (id)
    try: 
        categoria = Categoria.objects.get(pk=pk) 
    except Categoria.DoesNotExist: 
        return JsonResponse({'message': 'La categoría seleccionada no existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE categoria

    if request.method == 'GET': 
         categoria_serializer = CategoriaSerializer(categoria) 
         return JsonResponse(categoria_serializer.data) 
        
    elif request.method == 'PUT': 
        categoria_data = JSONParser().parse(request) 
        categoria_serializer = CategoriaSerializer(categoria, data=categoria_data) 
        if categoria_serializer.is_valid(): 
            categoria_serializer.save() 
            return JsonResponse(categoria_serializer.data) 
        return JsonResponse(categoria_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        categoria.delete() 
        return JsonResponse({'message': 'Has eliminado la categoría seleccionada'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def categoria_list_published(request):
     # GET todas las categorías 
    categorias = Categoria.objects.filter(published=True)
        
    if request.method == 'GET': 
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(categorias_serializer.data, safe=False)
