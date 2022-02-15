from django.db import models

# Create your models here.
class Productos (models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre 