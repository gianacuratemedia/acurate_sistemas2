from django.urls import path
from .views import GanaList, GanaDetail

urlpatterns = [
    path('all-tus-logros/', GanaList.as_view(), name="tus_logros"), #get all and post 
    path('all-tus-logros/<int:id>', GanaDetail.as_view(), name="tu_logro") #Get by id
    
]