from django.urls import path
from .views import EventoDetail, EventoList

urlpatterns = [
    path('all-eventos/', EventoList.as_view(), name="eventos"),
    path('all-eventos/<int:id>', EventoDetail.as_view(), name="evento")

]