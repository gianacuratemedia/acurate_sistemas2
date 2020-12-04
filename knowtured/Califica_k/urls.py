from django.urls import path
from .views import CalificaList, CalificaDetail

urlpatterns = [
    #Get lista de calificaciones que el alumno ha asignado a otros tutores 
    # post nueva calificación a otro tutor
    path('all-calificaciones/', CalificaList.as_view(), name="calificaciones"),
    #Only get and delate calificacion tutor
    path('all-calificaciones/<int:id>', CalificaDetail.as_view(), name="calificacion") 
    
]
