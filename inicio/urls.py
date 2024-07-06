from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("pacientes/", views.pacientes, name= "pacientes"),
    path("perros/ingreso/", views.ingresar_paciente, name= "ingresar_paciente"),
    path("perros/eliminar/<int:id>/", views.eliminar_paciente, name= "eliminar_paciente"),
    path("perros/editar/<int:id>/", views.editar_paciente, name= "editar_paciente"),
    path("perros/<int:id>/", views.ver_paciente, name= "ver_paciente"),
    ]
