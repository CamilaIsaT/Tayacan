from django.urls import path
from . import views

urlpatterns = [
    path('', views.tayacan, name='inicio'),
    path('colabora', views.sign_in, name='colabora'),
    path('nosotras', views.nosotras, name='nosotras'),
    path('saberes', views.saberes, name='saberes'),
    path('login', views.sesion, name='login'),
    path('registrarse', views.registrarse, name='registrarse'),
]