from django.contrib import admin
from django.urls import path
from mensaje import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', views.mensaje),
    path('nombre/', views.funcion_nombre),
]
