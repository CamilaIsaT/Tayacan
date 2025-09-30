from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#se define los diferentes roles que puede tener un usuario
class rol(models.Model):
    nombre_rol = models.CharField(max_length=50, unique=True, verbose_name='Nombre del rol')

    def __str__(self):
        return self.nombre_rol


class nivel_educacion(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre del nivel')

    def __str__(self):
        return self.nombre
#--------------------------------------------------------------   
#se define la tabla usuario
#Se extiende AbstractUser para heredar los campos predeterminados de Django (username, password, email, etc.)

class usuario(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_app_enciclopedia',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_app_enciclopedia',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
#Fecha de nacimiento es opcional (null=True, blank=True) porque solo se registra para estudiantes.
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
#Si un Rol se elimina, el campo 'rol' del Usuario se pone a NULL.
    rol= models.ForeignKey(rol, on_delete=models.SET_NULL, null=True, blank=True)
    nivel_educacion = models.ForeignKey(nivel_educacion, on_delete=models.SET_NULL, null=True, blank=True)
#verifica que el usuario es estudiante
    def es_estudiante(self):
        return self.rol and self.rol.nombre_rol == 'Estudiante'

    def __str__(self):
        return self.username

#--------------------------------------------------------------   
#se define la tabla de departamentos 
class departamento(models.Model):
#unique=True para que no se repitan los nombres de los departamentos
    nombre_departamento = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_departamento

#--------------------------------------------------------------   
#se define la tabla de categorias
class categoria(models.Model):
#unique=True para que no se repitan los nombres de las categorias
    nombre_categoria = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_categoria

#--------------------------------------------------------------
#se define la tabla de publicaciones
class publicacion(models.Model):
# Tupla que define las opciones para el tipo de publicación.
# Cada elemento es una tupla (valor_en_db, etiqueta_para_usuario).
# 'saberes' y 'museo' son los valores que se guardan en la base de datos.
# 'Publicación de saberes' y 'Museo Tayacan' son los textos que ve el usuario.


    FORMATOS=(
        ('saberes', 'Publicación de saberes'),
        ('museo', 'Museo Tayacán'),
    )
    titulo = models.CharField(max_length=200, verbose_name='Título')
    tipo_formato = models.CharField(max_length=20, choices=FORMATOS)
#balnk=True y null=True para que el contenido pueda ser opcional
#null=True en la base de datos si no tiene valor
    contenido = models.TextField()
    descripcion = models.TextField()
#'on_delete=models.CASCADE' significa que si se elimina un departamento, todos los objetos relacionados con ese departamento también serán eliminados automáticamente.
    departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(usuario, on_delete=models.CASCADE)
#'auto_now_add=True' establece automáticamente la fecha y hora actuales cuando se crea el objeto por primera vez.
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
#--------------------------------------------------------------
#se define la tabla de comentarios
class comentario(models.Model):
#'related_name' permite acceder a los comentarios de una publicación usando 'publicacion.comentarios.all()'
    publicacion = models.ForeignKey(publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(usuario, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
#retorna una representación legible del comentario, mostrando el autor y la publicación asociada.
        return f'Comentario de {self.autor.username} en {self.publicacion.titulo}'
    
#--------------------------------------------------------------
#se define la tabla de recursos multimedia
class imagen(models.Model):
#'related_name' permite acceder a las imágenes de una publicación usando 'publicacion.imagenes.all()'
    publicacion = models.ForeignKey(publicacion, on_delete=models.CASCADE, related_name='imagenes')
#'upload_to' especifica el directorio dentro de 'MEDIA_ROOT' donde se almacenarán las imágenes.
    imagen = models.ImageField(upload_to='publicaciones/', verbose_name='Imagen')

#retorna una representación legible de la imagen, mostrando la publicación asociada. 
    def __str__(self):
        return f'Imagen para {self.publicacion.titulo}'