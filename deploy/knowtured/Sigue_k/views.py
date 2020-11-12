from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Sigue
from .serializers import *
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def sigue_list(request):
    # GET lista de tutores que sigue el usuario, POST seguir a un tutor, DELETE dejar de seguir a un tutor
  if request.method == 'GET':
        sigues = Sigue.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            sigues = sigues.filter(title__icontains=title)
        
        sigues_serializer = SigueSerializer(sigues, many=True)
        return JsonResponse(sigues_serializer.data, safe=False)
       
  elif request.method == 'POST':
         
      sigue_data = JSONParser().parse(request)
      sigue_serializer = SigueSerializer(data=sigue_data)
      if sigue_serializer.is_valid():
        sigue_serializer.save()
        return JsonResponse(sigue_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(sigue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
      elif request.method == 'DELETE':
        count = Sigue.objects.all().delete()
        return JsonResponse({'message': '{} Los tutores a los que sigues han sido eliminados'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
@api_view(['GET', 'PUT', 'DELETE'])
def sigue_detail(request, pk):
    # find sigue by pk (id)
    try: 
        sigue = Sigue.objects.get(pk=pk) 
    except Sigue.DoesNotExist: 
        return JsonResponse({'message': 'No sigues al tutor seleccionado'}, status=status.HTTP_404_NOT_FOUND) 
         
          # GET / PUT / DELETE sigue
    if request.method == 'GET': 
         sigue_serializer = SigueSerializer(sigue) 
         return JsonResponse(sigue_serializer.data) 
        
    elif request.method == 'PUT': 
        sigue_data = JSONParser().parse(request) 
        sigue_serializer = SigueSerializer(sigue, data=sigue_data) 
        if sigue_serializer.is_valid(): 
            sigue_serializer.save() 
            return JsonResponse(sigue_serializer.data) 
        return JsonResponse(sigue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE': 
        sigue.delete() 
        return JsonResponse({'message': 'Has dejado de seguir a este usuario'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def sigue_list_published(request):
     # GET todos los tutores que sigues
    sigues = Sigue.objects.filter(published=True)
        
    if request.method == 'GET': 
        sigues_serializer = SigueSerializer(sigues, many=True)
        return JsonResponse(sigues_serializer.data, safe=False)