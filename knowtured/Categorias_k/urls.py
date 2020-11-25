from django.urls import path
from .views import CategoriaDetail
from .views import CategoriaList, CategoriaListP


urlpatterns = [
    path('all-categorias/', CategoriaList.as_view(), name="categorias"),
    path('all-categorias/<int:id>', CategoriaDetail.as_view(), name="categoria"),
    path('', CategoriaListP.as_view(), name="all_categorias")
]
