from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):

    grupo1 = Estudiante.objects.filter(grupo = 1)
    grupo4 = Estudiante.objects.filter(grupo = 4)
    estudiantes = Estudiante.objects.all()
    
    # Estudiantes con el mismo apellido: Mendoza
    apMendoza = Estudiante.objects.filter(apellidos = 'Mendoza')

    # Estudiantes con la misma edad: 22
    edad22 = Estudiante.objects.filter(edad = 22)

    # Estudiantes del grupo 3 con la misma edad: 22
    grupo3Edad22 = Estudiante.objects.filter(grupo = 3, edad = 22)

    return render(request, 'index.html', {'grupo1':grupo1, 'grupo4':grupo4, 'mismoApellido':apMendoza, 'mismaEdad':edad22, 'grupo3MismaEdad':grupo3Edad22, 'estudiantes': estudiantes})
    