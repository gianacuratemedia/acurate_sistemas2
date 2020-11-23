 
from django.contrib import admin
from django.urls import path

from counter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('users/', include('Usuarios_k.urls')),
    path('categorias/', include('Categorias_k.urls'))
]
