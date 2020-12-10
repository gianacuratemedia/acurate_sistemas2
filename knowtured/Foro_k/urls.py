from django.urls import path
from .views import ForoList, ForoDetail, ForoList_Curso_GP
from .views import ComentarioList, ComentarioList_Curso_Foro_GP, ComentarioDetail

urlpatterns = [
#Get foros creados por el usuario
    path('tus-foros/', ForoList.as_view(), name="foro_user"),
#Get and post foro por url del curso
    path('curso/<int:curso_id>', ForoList_Curso_GP.as_view(), name="foro_curso"),
 #Get and delete by curso_id and foro_id
    path('curso/<int:curso_id>/foro/<int:id>', ForoDetail.as_view(), name="foro_detail"),

#Publicaciones o mensajes
#Get comentarios publicados por el usuario
    path('tus-comentarios-en-foros/', ComentarioList.as_view(), name="comentarios_user"),
#Get and post comentarios por url de foro_id
    path('foro/<foro_id>/comentarios/', ComentarioList_Curso_Foro_GP.as_view(), name="comentarios_curso"),
#Update and delete mensaje por id del mensaje
    path('foro/<foro_id>/comentarios/<int:id>', ComentarioDetail.as_view(), name="comentarios_id-mensaje")

]
