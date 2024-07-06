from django.db import models

class Perro(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    edad = models.IntegerField()
    #fecha_vacunacion = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.raza}"
