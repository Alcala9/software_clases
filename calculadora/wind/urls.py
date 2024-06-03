from django.urls import path
from .views import funcion_hola, funcion_calcualdora

urlpatterns = [
    path('hola/', funcion_hola),
    path('calculadora/', funcion_calcualdora),
]
