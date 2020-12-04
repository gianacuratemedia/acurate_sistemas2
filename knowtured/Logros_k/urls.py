from django.urls import path
from .views import LogroDetail, LogroList

urlpatterns = [
    path('all-logros/', LogroList.as_view(), name="logros"), #get all and create 
    path('all-logros/<int:id>', LogroDetail.as_view(), name="logro") #Get, update, delete by id
    
]