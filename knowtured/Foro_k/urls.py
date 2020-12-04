from django.urls import path
from .views import ForoList, ForoDetail


urlpatterns = [
#Get mensajes publicados por usuario y post un mensaje en 
    path('all-tus-mensajes/', ForoList.as_view(), name="mensajes_user"),

#Get mensajes o publicaciones por id_curso
    path('all-cursos/<int:curso_id>', ForoDetail.as_view(), name="mensajes_curso"),
#Update and delete mensaje por id del mensaje
    path('all-cursos/<int:id>', ForoDetail.as_view(), name="mensajes_id-mensaje")

]