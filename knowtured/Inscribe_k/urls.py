from django.urls import path
from .views import InscripcionView, InscripcionDetail

urlpatterns = [
    path('inscribete/', InscripcionView.as_view(), name="inscripciones"),
    path('inscribete/<int:id>', InscripcionDetail.as_view(), name="inscripcion") #Only post and delate
    
]
