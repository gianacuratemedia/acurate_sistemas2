from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CategoriasSerializer
from .models import Categoria
from rest_framework import permissions
from .permissions import IsOwner


class CategoriaListAPIView(ListCreateAPIView):
    serializer_class = CategoriasSerializer
    queryset = Categoria.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CategoriaDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriasSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Categoria.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
