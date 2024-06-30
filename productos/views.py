from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Accesorio
from django.urls import reverse_lazy

class Accesorios(ListView):
    model = Accesorio
    template_name = "accesorios/listado_de_accesorios.html"
    context_object_name = "accesorios"
    
class CrearAccesorio(CreateView):
    model = Accesorio
    template_name = "accesorios/crear_accesorio.html"
    success_url = reverse_lazy("accesorios")
    fields = ["tipo", "talle", "color"]
    
class EditarAccesorio(UpdateView):
    ...
    

class VerAccesorio(DetailView):
    model = Accesorio
    template_name = "accesorios/ver_accesorio.html"
    
    