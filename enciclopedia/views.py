from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
 

# Create your views here.


def tayacan(request):
    return render(request, "paginas/tayacan.html")

def sign_in(request):
    return render(request, "inicio sesion/perfilnt.html")

def registrarse(request):
    return render(request, "inicio sesion/registrarse.html")

def sesion(request):
    return render(request, "inicio sesion/login.html")

def nosotras(request):
    return render(request, "paginas/nosotras.html")

def saberes(request):
    return render(request, "paginas/saberes.html")


