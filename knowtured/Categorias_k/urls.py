from django.urls import path
from .views import CategoriaListAPIView, CategoriaDetailAPIView


urlpatterns = [
    path('', CategoriaListAPIView.as_view(), name="categorias"),
    path('<int:id>', CategoriaDetailAPIView.as_view(), name="categoria")
]
