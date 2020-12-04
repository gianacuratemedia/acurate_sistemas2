from django.urls import path
from .views import *

urlpatterns = [
    path('all-actividades/', RealizaList.as_view(), name="actividades"), #get and post (alumnos)
    path('all-actividades/<int:id>', RealizaDetail.as_view(), name="actividad"), #Get, update, delete by id (alumnos)
    path('all-actividades-contenido/', AsignarCalificaciones.as_view(), name="actividades"), #get actividad por contenido_id (tutor)
    path('all-actividades-contenido/<int:id>', RealizaUpdateC.as_view(), name="actividad") #Update calificacion (tutor)
]