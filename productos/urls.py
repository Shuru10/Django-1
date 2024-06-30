from django.urls import path
from . import views

urlpatterns = [
    path("accesorios/", views.Accesorios.as_view(), name="accesorios"),
    path("accesorios/crear/", views.CrearAccesorio.as_view(), name="crear_accesorio"),
    path("accesorios/<int:pk>/", views.VerAccesorio.as_view(), name="ver_accesorio"),
    
]
