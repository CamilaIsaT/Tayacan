from django.urls import path
from . import views

urlpatterns = [
    path('', views.tayacan, name='inicio'),
    path('colabora', views.sin_perfil, name='colabora'),
     path('login', views.iniciar_sesion, name='login'),
    path('registrarse', views.registrarse, name='registrarse'),
     path('publicar', views.colaborador, name='publicar'),
    path('nosotras', views.nosotras, name='nosotras'),
    path('saberes', views.saberes, name='saberes'),
    path('categoria', views.categoria, name='categoria'),
   

]