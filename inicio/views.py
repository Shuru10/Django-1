from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from inicio.models import Perro
from inicio.forms import IngresarPacienteFormulario, BuscarPaciente, EditarPacienteFormulario
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio/index.html")

def crear_perro(request, nombre, raza, edad):
    perro = Perro(nombre=nombre, raza=raza, edad=edad)
    perro.save()
    return render(request, "perro_template/creacion.html", {"perro": perro})

def ingresar_paciente(request):
    formulario = IngresarPacienteFormulario()

    if request.method == "POST":
        formulario = IngresarPacienteFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            perro = Perro(nombre=datos.get("nombre"), raza=datos.get("raza"), edad=datos.get("edad"))
            perro.save()
            return redirect("pacientes")

    return render(request, "inicio/ingresar_paciente.html", {"formulario": formulario})

def pacientes(request):
    formulario = BuscarPaciente(request.GET)
    pacientes = []
    if formulario.is_valid():
        nombre = formulario.cleaned_data["nombre"]
        pacientes = Perro.objects.filter(nombre__icontains=nombre)

    return render(request, "inicio/pacientes.html", {"pacientes": pacientes, "formulario": formulario})

@login_required
def eliminar_paciente(request, id):
    perro = get_object_or_404(Perro, id=id)
    perro.delete()
    return redirect("pacientes")

@login_required
def editar_paciente(request, id):
    perro = get_object_or_404(Perro, id=id)
    
    formulario = EditarPacienteFormulario(initial={"nombre": perro.nombre, "raza": perro.raza, "edad": perro.edad})
    
    if request.method == "POST":
        formulario = EditarPacienteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            perro.nombre = info["nombre"]
            perro.raza = info["raza"]
            perro.edad = info["edad"]
            perro.save()
            return redirect("pacientes")

    return render(request, "inicio/editar_paciente.html", {"formulario": formulario, "perro": perro})

def ver_paciente(request, id):
    perro = get_object_or_404(Perro, id=id)
    return render(request, "inicio/ver_paciente.html", {"perro": perro})
