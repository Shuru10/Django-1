from django.urls import path
from inicio import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("template1/<str:nombre>/<str:apellido>/<int:edad>", views.template1),
    path("template2/<str:nombre>/<str:apellido>/<int:edad>", views.template2),
    path("template3/<str:nombre>/<str:apellido>/<int:edad>", views.template3),
    path("template4/<str:nombre>/<str:apellido>/<int:edad>", views.template4),
    path("probando/", views.probando, name="probando"),
    path("perros/crear/<str:nombre>/<str:raza>/<int:edad>/", views.crear_perro, name= "crear_perro")
    ]
    