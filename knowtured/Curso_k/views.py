from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import CursoSerializer, CursoSerializerP, ContenidoSerializer, PublicContenidoSerializer, CursoSerializerr, InfoCursoPay, InfoContenidoPay
from .serializers import ShowIdContenido
from .models import Curso, Contenido, Contenido_Usuario
from Categorias_k.models import Categoria
from Usuarios_k.models import User
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.db.models import Q
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.db.models import Sum

class CursoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CursoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id, categoria_id):
        try:
            curso = Curso.objects.get(id=id, categoria_id=categoria_id)
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso

    # Get un curso
    def get(self, request, id, categoria_id):

        curso = self.get_queryset(id, categoria_id)
        serializer = CursoSerializer(curso)
            #Agregar campo actualizar no_vistas
        curso_v = Curso.objects.get(id=id)
        result=curso_v.no_vistas
        if result is None:
            result=1
            curso_v.no_vistas=result
            curso_v.save()
        if not result is None:
            curso_v.no_vistas=curso_v.no_vistas+1
            curso_v.save()
        
        #Vistas trimestrales 
        if result2 is None:
            result2=1
            curso_v.no_vistas_t=result2
            curso_v.save()
        if not result2 is None:
            curso_v.no_vistas_t=curso_v.no_vistas_t+1
            curso_v.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un curso
    def put(self, request, id, categoria_id):
        
        curso = self.get_queryset(id, categoria_id)

        if(request.user == curso.owner): # Si el creador del curso en quien hace el request
            serializer = CursoSerializer(curso, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un curso
    def delete(self, request, id, categoria_id):

        curso = self.get_queryset(id, categoria_id)

        if(request.user == curso.owner): # Si el creador es quien hace el request
            curso.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

#View Get and post Curso por parametro categoria 
class CursoList_Categoria_GP(ListCreateAPIView):
    serializer_class = CursoSerializerr
    queryset = Curso.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        categoria_id=self.kwargs['categoria_id']
        try:
            curso = Curso.objects.all().filter(categoria_id=categoria_id)
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso

    # Create un nuevo curso por categoria
       
    def post(self, request, *args, **kwargs):
        categoria_id= Categoria.objects.get(id=self.kwargs['categoria_id'])
        serializer = CursoSerializerr(data=request.data)
        if serializer.is_valid():
             serializer.save(owner=self.request.user, categoria_id=categoria_id)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#View todos los cursos creados por un usuario 
class CursoList(ListAPIView):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)





#Cursos por categoria_id
@permission_classes((AllowAny, ))
class Curso_Categoria_List(ListAPIView):

    def get_queryset(self, categoria_id):
        try:
            curso = Curso.objects.get(categoria_id=categoria_id)
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso


#LISTA SIN PERMISO DE AUTENTIFICACIÓN

@permission_classes((AllowAny, ))
class CursoListP(ListAPIView):
       serializer_class = CursoSerializerP
       queryset = Curso.objects.all()




#VIEWS CONTENIDO DE CURSO

class ContenidoDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ContenidoSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)

    def get_queryset(self, id, curso_id):
        try:
            contenido = Contenido.objects.get(id=id, curso_id=curso_id)
        except Contenido.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return contenido

    # Get un contenido
    def get(self, request, id, curso_id):

        contenido = self.get_queryset(id, curso_id)
        serializer = ContenidoSerializer(contenido)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update un contenido
    def put(self, request, id, curso_id):
        
        contenido = self.get_queryset(id, curso_id)

        if(request.user == contenido.owner==Curso.owner): # If creator is who makes request
            serializer = ContenidoSerializer(contenido, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete un contenido
    def delete(self, request, id, curso_id):

        contenido = self.get_queryset(id, curso_id)
        

        if(request.user == contenido.owner==Curso.owner): # If creator is who makes request
            contenido.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class ContenidoList(ListCreateAPIView):
    serializer_class = ContenidoSerializer
    queryset = Contenido.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        curso_id=self.kwargs['curso_id']
        try:
            contenido = Contenido.objects.all().filter(curso_id=curso_id)
        except Contenido.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return contenido

    # Create un nuevo contenido por curso
       
    def post(self, request,*args, **kwargs,):
        curso_id= Curso.objects.get(id=self.kwargs['curso_id'])
        serializer = ContenidoSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save(owner=self.request.user, curso_id=curso_id)
             
             try:
                   contenido_user=Contenido_Usuario.objects.get(owner=self.request.user)
                   contenido_user.contenido_trimestral=contenido_user.contenido_trimestral+1
                   contenido_user.save()
                   
       
             except Contenido_Usuario.DoesNotExist:
                   contenido_user = Contenido_Usuario.objects.create(
                   owner=self.request.user,
                   contenido_trimestral=1
                   )
                   
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#LISTA SIN PERMISO DE AUTENTIFICACIÓN

@permission_classes((AllowAny, ))
class ContenidoListP(ListAPIView):
       serializer_class = PublicContenidoSerializer
       queryset = Contenido.objects.all().order_by('curso_id')



#Barra de busqueda curso por nombre o descripcion

class BusquedaCurso(ListAPIView):
    serializer_class = CursoSerializerr
    queryset = Curso.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self,*args, **kwargs):
        busqueda=self.kwargs['busqueda']
        try:
            curso = Curso.objects.all().filter(
            Q(nombre__icontains=busqueda) 
            | Q(descripcion__icontains=busqueda)
            )
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso


#Consultar información de todos los cursos obteniendo el nombre del curso, user y no de vistas 
 
@permission_classes((AllowAny, ))
class CursoPayment(ListAPIView):
       serializer_class = InfoCursoPay
       queryset = Curso.objects.all().order_by('no_vistas_t')
    

#Consultar cantidad de contenido creado por usuario
@permission_classes((AllowAny, ))
class ContenidoPayment(ListAPIView):
       serializer_class = InfoContenidoPay
       queryset = Contenido_Usuario.objects.all().order_by('contenido_trimestral')


#Mostrar la lista con id de contenido realizado 

@api_view(['GET'])
def Contenido_ids(request):
    serializer_class = ShowIdContenido
    results = list(Contenido_Usuario.objects.values())

    return JsonResponse({'results':results}, safe=False)


#View contar contenido total creado:

@api_view(['GET'])
def Contenido_total_i(request):
    total_contenido = Contenido_Usuario.objects.aggregate(Sum('contenido_trimestral'))

    return Response(total_contenido)

#View obtener cantidad de contenido trimestral realizado por id de usuario
class Contenido_Usuario_Detail(ListAPIView):
    serializer_class = InfoContenidoPay

    def get_queryset(self, owner):
        try:
            contenido_u = Contenido_Usuario.objects.get(owner=owner)
        except Contenido_Usuario.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return contenido_u

    # Get info por id
    def get(self, request, owner):

        contenido_u = self.get_queryset(owner)
        serializer = InfoContenidoPay(contenido_u)
        return Response(serializer.data, status=status.HTTP_200_OK)



#View consultar todos los cursos y las vistas trimestrales por usuario: id_owner y vistas trimestrales 
@api_view(['GET'])
def Vistas_Cursos_ids(request):
    serializer_class = InfoCursoPay
    results = list(Curso.objects.values())

    return JsonResponse({'results':results}, safe=False)

#View consultar vistas trimestrales totales de todos los cursos 

@api_view(['GET'])
def Curso_total_i(request):
    total_curso = Curso.objects.aggregate(Sum(' no_vistas_t'))

    return Response(total_curso)



#View obtener cantidad total de vistas trimestrales por todos los cursos realizados por usuario
class Curso_Usuario_Detail(ListAPIView):
    serializer_class = InfoCursoPay

    def get_queryset(self, owner):
        try:
            curso_u = Curso.objects.filter(owner=owner).aggregate(Sum('no_vistas_t'))
        
        except Curso.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return curso_u

    # Get info por id
    def get(self, request, owner):

        curso_u = self.get_queryset(owner)
        serializer = InfoCursoPay(curso_u)
        return Response(serializer.data, status=status.HTTP_200_OK)




#Descargar archivo

#class DocumentDownload(View): 
    #permission_classes = (permissions.IsAuthenticated,)

    
    #def get(self, request, relative_path):
        #document =Contenido.objects.all().filter(archivo_ubc=relative_path)
        #absolute_path = '{}/{}'.format(settings.MEDIA_ROOT, relative_path)
        #response = FileResponse(open(absolute_path, 'rb'), as_attachment=True)
        #return response
