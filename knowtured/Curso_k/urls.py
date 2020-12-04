from django.urls import path
from .views import CursoDetail, CursoList, CursoListP
from .views import ContenidoDetail
from .views import ContenidoList, ContenidoListP

urlpatterns = [
    path('all-cursos/', CursoList.as_view(), name="cursos"),
    path('all-cursos/<int:id>', CursoDetail.as_view(), name="curso"),
    path('', CursoListP.as_view(), name="all_categorias"),

    #Contenido de los cursos
    path('all-contenido/', ContenidoList.as_view(), name="contenidos"),
    path('all-contenido/<int:id>', ContenidoDetail.as_view(), name="contenido-curso"),
    path('', ContenidoListP.as_view(), name="all_contenido")
    
]
