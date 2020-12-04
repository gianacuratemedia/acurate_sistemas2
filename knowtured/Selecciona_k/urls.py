from django.urls import path
from .views import SeleccionaList, SeleccionaDetail

urlpatterns = [
    path('all-seleccion/', SeleccionaList.as_view(), name="seleccion-all"), #get and post
    path('all-seleccion/<int:id>', SeleccionaDetail.as_view(), name="seleccion") #Get and delete by id 
]