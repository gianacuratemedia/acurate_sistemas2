from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CategoriasSerializer
from .models import Categoria
from rest_framework import permissions
from .permissions import IsOwner


class CategoriaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriasSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            categoria = Categoria.objects.get(id=id)
        except Categoria.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return categoria

    # Get una categoria
    def get(self, request, id):

        categoria = self.get_queryset(id)
        serializer = CategoriasSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update una categoria
    def put(self, request, id):
        
        categoria = self.get_queryset(id)

        if(request.user == categoria.owner): # If creator is who makes request
            serializer = CategoriasSerializer(categoria, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete una categoria
    def delete(self, request, id):

        categoria = self.get_queryset(id)

        if(request.user == categoria.owner): # If creator is who makes request
            categoria.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class CategoriaList(ListCreateAPIView):
    serializer_class = CategoriasSerializer
    queryset = Categoria.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Create una nueva categoria
    def post(self, request):
        serializer = CategoriasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

