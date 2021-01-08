from django.contrib import admin
from .models import Curso, Contenido, Contenido_Usuario

admin.site.register(Curso)
admin.site.register(Contenido)
admin.site.register(Contenido_Usuario)
