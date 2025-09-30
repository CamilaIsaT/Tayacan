from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import rol, usuario, departamento, categoria, comentario, publicacion, imagen, nivel_educacion;
from .forms import rol_educador, rol_estudiante, EducRegistro, EstuRegistro

# Create your views here.


def tayacan(request):
    return render(request, "paginas/tayacan.html")

def sin_perfil(request):
    return render(request, "inicio sesion/sinperfil.html")

from django.shortcuts import render, redirect
from .forms import EducRegistro, EstuRegistro

def registrarse(request):
    form_educador = EducRegistro()
    form_estudiante = EstuRegistro()
    if request.method == "POST":
        # Si viene del form de educador
        if "form-educador" in request.POST:
            form_educador = EducRegistro(request.POST)
            if form_educador.is_valid():
                form_educador.save(user_role_name="Educador")
                return redirect("login")
        elif "form-estudiante" in request.POST:
            form_estudiante = EstuRegistro(request.POST)
            if form_estudiante.is_valid():
                form_estudiante.save(user_role_name="Estudiante")
                return redirect("login")
    
    return render(request, "inicio sesion/registrarse.html", {
        "form_educador": form_educador,
        "form_estudiante": form_estudiante,
    })


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


