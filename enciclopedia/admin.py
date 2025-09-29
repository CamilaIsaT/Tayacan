from django.contrib import admin

# Register your models here.
from .models import rol, usuario, departamento, categoria, publicacion, comentario, imagen

# Registra todos los modelos que deseas gestionar desde el admin
admin.site.register(rol)
admin.site.register(usuario)
admin.site.register(departamento)
admin.site.register(categoria)
admin.site.register(publicacion)
admin.site.register(comentario)
admin.site.register(imagen)