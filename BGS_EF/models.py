from django.db import models

# Create your models here.
class Docente(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    Fecha_nacimiento = models.DateField()
    Fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=100)

class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    horas = models.CharField(max_length=100)
    creditos = models.IntegerField()
    Fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=100)
