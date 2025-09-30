from django.contrib import admin

# Register your models here.
from .models import rol, usuario, departamento, categoria,  comentario, publicacion, imagen, nivel_educacion;

admin.site.register(rol)
admin.site.register(usuario)
admin.site.register(departamento)
admin.site.register(categoria)
admin.site.register(comentario)
admin.site.register(publicacion)
admin.site.register(imagen)
admin.site.register(nivel_educacion)
