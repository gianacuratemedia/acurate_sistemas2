from django.urls import path
from .views import CuponList, CuponDetail


urlpatterns = [
    path('all-cupones/', CuponList.as_view(), name="cupones"),
    path('all-cupones/<int:id>', CuponDetail.as_view(), name="cupon")

]
