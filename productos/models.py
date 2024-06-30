from django.db import models

# Create your models here.

class Accesorio(models.Model):  #aca va en singular
    tipo = models.CharField(max_length=100)
    talle = models.IntegerField()
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.tipo} {self.talle}"