from django.urls import path
from Curso_k import views
from .views import CursoDetail, CursoList, CursoListP, BusquedaCurso
from .views import ContenidoDetail, Contenido_Usuario_Detail, Curso_Usuario_Detail
from .views import ContenidoList, ContenidoListP, Curso_Categoria_List, CursoList_Categoria_GP, CursoPayment, ContenidoPayment

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
    path('all-cursos/buscar/<str:busqueda>',BusquedaCurso.as_view(), name="curso_busqueda"),

    #Todos los cursos por nombre, user y no de visitas 
    path('all-cursos/estadisticas/vistas/',CursoPayment.as_view(), name="curso_estadisticas"),
    #Contabilizar cantidad de contenido trimestral 
    path('all-cursos/estadisticas/contenido/',ContenidoPayment.as_view(), name="contenido_estadisticas"),

    #ID's usuarios contenido
    path('all-cursos/estadisticas/contenido/ids/', views.Contenido_ids),
    #suma total contenido
    path('all-cursos/estadisticas/contenido/total/', views.Contenido_total_i),

    #Cantidad de contenido total creado por usuario 
    path('all-cursos/estadisticas/contenido/total/<int:owner>',Contenido_Usuario_Detail.as_view(), name="no_contenido_user"),

    #Obteniendo datos de cursos y vistas trimestrales 
    path('all-cursos/estadisticas/cursos/ids/', views.Vistas_Cursos_ids),   

    #Suma de todas las vistas trimestrales totales de los cursos 
    path('all-cursos/estadisticas/cursos/total/', views.Curso_total_i),

    #Cantidad de vistas trimestrales totales creadas por usuario
    path('all-cursos/estadisticas/contenido/total/<int:owner>',Curso_Usuario_Detail.as_view(), name="no_vistas_curso_user"),

]
