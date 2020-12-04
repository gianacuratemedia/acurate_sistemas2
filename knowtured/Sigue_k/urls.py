from django.urls import path
from .views import SigueList, SigueDetail

urlpatterns = [
    path('sigue/', SigueList.as_view(), name="sigues"),
    path('sigue/<int:id>', SigueDetail.as_view(), name="sigue") #Only post and delate
    
]
