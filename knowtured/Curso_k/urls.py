from django.urls import path
from .views import CursoDetail, CursoList, CursoListP


urlpatterns = [
    path('all-cursos/', CursoList.as_view(), name="cursos"),
    path('all-cursos/<int:id>', CursoDetail.as_view(), name="curso"),
    path('', CursoListP.as_view(), name="all_categorias")
]

