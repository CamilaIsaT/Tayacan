from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("<h1> Hola, mundo. Estás en la página de inicio de la enciclopedia.</h1>")

def tayacan(request):
    return render(request, "paginas/tayacan.html")
