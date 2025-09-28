from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
 

# Create your views here.


def tayacan(request):
    return render(request, "paginas/tayacan.html")

def sin_perfil(request):
    return render(request, "inicio sesion/sinperfil.html")

def registrarse(request):
    return render(request, "inicio sesion/registrarse.html")

def iniciar_sesion(request):
    return render(request, "inicio sesion/iniciar.html")

def nosotras(request):
    return render(request, "paginas/nosotras.html")

def saberes(request):
    return render(request, "paginas/saberes.html")

def colaborador(request):
    return render(request, "paginas/colabora.html")

def categoria(request):
    return render(request, "saberes/categoria.html")


