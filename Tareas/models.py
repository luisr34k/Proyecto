
from django.db import models

class Profesor(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=[('M', 'Macho'), ('F', 'Hembra')])
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return self.nombre