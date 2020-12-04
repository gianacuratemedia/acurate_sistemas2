from django.urls import path
from .views import ExperienciaDetail, ExperienciaList

urlpatterns = [
    path('all-experiencia/', ExperienciaList.as_view(), name="all_experiencia"),
    path('all-experiencia/<int:id>', ExperienciaDetail.as_view(), name="experiencia")

]