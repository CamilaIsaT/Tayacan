from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tayacan', views.tayacan, name='tayacan'),
]