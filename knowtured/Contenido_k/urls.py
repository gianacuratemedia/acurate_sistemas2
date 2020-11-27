from django.urls import path
from .views import ContenidoDetail
from .views import ContenidoList, ContenidoListP


urlpatterns = [
    path('all-contenido/', CategoriaList.as_view(), name="contenidos"),
    path('all-contenido/<int:id>', ContenidoDetail.as_view(), name="contenido-curso"),
    path('', ContenidoListP.as_view(), name="all_contenido")
]
