from django.shortcuts import render

def funcion_hola(request):
    return render(request, 'hola.html')

def funcion_calcualdora(request):
    return render(request, 'calculadora.html')
