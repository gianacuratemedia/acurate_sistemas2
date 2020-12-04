from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CuponSerializer
from .models import Cupon
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

class CuponDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CuponSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id):
        try:
            cupon = Cupon.objects.get(id=id)
        except Cupon.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return cupon

    # Get una cupon
    def get(self, request, id):

        cupon = self.get_queryset(id)
        serializer = CuponSerializer(cupon)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un cupon
    def put(self, request, id):
        
        cupon = self.get_queryset(id)

        if(request.user == cupon.owner): # If creator is who makes request
            serializer = CuponSerializer(cupon, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un cupon
    def delete(self, request, id):

        cupon = self.get_queryset(id)

        if(request.user == cupon.owner): # If creator is who makes request
            cupon.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class CuponList(ListCreateAPIView):
    serializer_class = CuponSerializer
    queryset = Cupon.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    # Create un cupon
    def post(self, request):
       
        serializer = CuponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
