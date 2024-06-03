from django.shortcuts import render

def mensaje(request):
    return render(request, 'mensaje.html')

def funcion_nombre(request):
    nombre = 'Uriel'
    return render(request, 'nombre.html',{'nombre':nombre})
    