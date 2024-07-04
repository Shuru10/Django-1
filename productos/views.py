from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Accesorio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Accesorios(ListView):
    model = Accesorio
    template_name = "accesorios/listado_de_accesorios.html"
    context_object_name = "accesorios"
    
class CrearAccesorio(CreateView):
    model = Accesorio
    template_name = "accesorios/crear_accesorio.html"
    success_url = reverse_lazy("accesorios")
    fields = ["tipo", "talle", "color"]
    
class EditarAccesorio(LoginRequiredMixin, UpdateView):
    model = Accesorio
    template_name = "accesorios/editar_accesorio.html"
    success_url = reverse_lazy("accesorios")
    fields = ["tipo", "talle", "color"]
    

class VerAccesorio(DetailView):
    model = Accesorio
    template_name = "accesorios/ver_accesorio.html"
    
class EliminarAccesorio(LoginRequiredMixin, DeleteView):
    model = Accesorio
    template_name = "accesorios/eliminar_accesorio.html"
    success_url = reverse_lazy("accesorios")

    
    