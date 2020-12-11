from django.urls import path
from .views import CursoDetail, CursoList, CursoListP, BusquedaCurso
from .views import ContenidoDetail
from .views import ContenidoList, ContenidoListP, Curso_Categoria_List, CursoList_Categoria_GP

urlpatterns = [
    #Lista de todos los cursos por el usuario que hace la petición get 
    path('all-cursos/', CursoList.as_view(), name="cursos"),
    #Get curso por categoria y curso que el usuario ha hecho y post usando el parametro de la categoria
    path('all-cursos/categoria/<int:categoria_id>', CursoList_Categoria_GP.as_view(), name="curso_categoria"),
    #Get, update and delete by id del curso and categoria_id
    path('all-cursos/categoria/<int:categoria_id>/<int:id>', CursoDetail.as_view(), name="curso"),
    path('', CursoListP.as_view(), name="all_cursos"),
    #List cursos por categoria sin permisos
    path('all-cursos/categorias/<int:categoria_id>', Curso_Categoria_List.as_view(), name="curso_categoria_p"),

    #Contenido de curso por id_curso
    # Get y post 
    # Post con curso_id 
    path('all-cursos/<int:curso_id>/all-contenido/', ContenidoList.as_view(), name="contenido_por_curso"),
    #Get, update and delete by curso_id and id_contenido
    path('all-cursos/<int:curso_id>/all-contenido/<int:id>', ContenidoDetail.as_view(), name="contenido-curso"),
    #Get contenido filtrado por curso sin permiso
    path('', ContenidoListP.as_view(), name="all_contenido"),
    #Busqueda curso por nombre
    path('all-cursos/buscar/<str:busqueda>',BusquedaCurso.as_view(), name="curso_busqueda")
    
]
