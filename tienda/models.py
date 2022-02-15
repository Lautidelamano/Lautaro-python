from django.db import models

# Create your models here.
class autos (models.Model):
    marca = models.CharField(max_length=20)
    descrip = models.CharField(max_length=150)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return self.marca 