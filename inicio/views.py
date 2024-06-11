from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context

def inicio(request):
    return HttpResponse("Bienvenidos a mi Inicio")

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    return HttpResponse(f"<h1>Mi Template 1</h1> -- Fecha:{fecha} -- Bienvenido {nombre} {apellido} {edad}")

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r"C:\Users\joaco\Desktop\Python\Proyecto Django-1\templates\template2.html")
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close()
    fecha = datetime.now()
    
    datos = {
        "fecha":fecha,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        }
    
    contexto = Context(datos)
    
    Template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)