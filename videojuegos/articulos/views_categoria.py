from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from articulos.models import Categoria, Articulos
from articulos.forms import FormCategoria
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaCategorias(ListView):
    model = Categoria
    queryset = Categoria.objects.order_by('nombre')

class NuevaCategoriaView(CreateView):
    model = Categoria
    #fields = '__all__'
    form_class = FormCategoria
    success_url = (reverse_lazy('categorias_lista'))
    extra_context = {'accion':'Nueva'}

class EditarCategoriaView(UpdateView):
    model = Categoria
    fields = '__all__'
    success_url = (reverse_lazy('categorias_lista'))
    extra_context = {'accion':'Modificar'}

class EliminarCategoriaView(DeleteView):
    model = Categoria
    success_url = (reverse_lazy('categorias_lista'))

    def form_valid(self,form):
        self.object = self.get_object()
        print(self.object) 
        if Articulos.objects.filter(categoria=self.object):
            messages.error(self.request, 'No se puede eliminar la categoría; tiene artículos agregados')
        else:
            self.object.delete()
            messages.success(self.request, 'La categoría se eliminó con éxito ')
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)


class BienvenidaView(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'



 