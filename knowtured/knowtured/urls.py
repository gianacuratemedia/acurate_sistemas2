"""djangoreactproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
   path('users/', include('Usuarios_k.urls')),
    path('categorias/', include('Categorias_k.urls')),
    path('cursos/', include('Curso_k.urls')),
    path('inscripciones/', include('Inscribe_k.urls')),
    path('eventos/', include('Evento_k.urls')),
    path('logros/', include('Logros_k.urls')),
    path('cupones/', include('Cupon_k.urls')),
    path('tutores/', include('Sigue_k.urls')),
    path('experiencia/', include('Experiencia_k.urls')),
    path('realiza/', include('Realiza_k.urls')),
    path('califica/', include('Califica_k.urls')),
    path('selecciona/', include('Selecciona_k.urls')),
    path('gana/', include('Gana_k.urls')),
    path('foros/', include('Foro_k.urls'))
  

]
