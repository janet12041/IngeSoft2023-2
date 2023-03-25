from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def getMismoApellido(list):

    list = list.order_by('apellidos')
    listMismos = []
    for i in range(0, len(list)):
        if i < len(list)-1 and list[i].apellidos == list[i+1].apellidos:
           listMismos.append(list[i])
        elif i != 0 and list[i].apellidos == list[i-1].apellidos:
            listMismos.append(list[i])
    return listMismos

def getMismaEdad(list):
    list = list.order_by('edad')
    listMismos = []
    for i in range(0, len(list)):
        if i < len(list)-1 and list[i].edad == list[i+1].edad:
            listMismos.append(list[i])
        elif i != 0 and list[i].edad == list[i-1].edad:
            listMismos.append(list[i])  
    return listMismos  

def index(request):

    #Get cuando se sabe que hay un dato único
    #Filter regresa una lista de todos los datos de la consulta
    grupo1 = Estudiante.objects.filter(grupo = 1)
    grupo4 = Estudiante.objects.filter(grupo = 4)
    grupo3 = Estudiante.objects.filter(grupo = 3)
    estudiantes = Estudiante.objects.all()
    mismoApellido = getMismoApellido(estudiantes)
    mismaEdad = getMismaEdad(estudiantes)   
    grupo3MismaEdad = getMismaEdad(grupo3)
    

    return render(request, 'index.html', {'grupo1':grupo1, 'grupo4':grupo4,'inOrder':grupo3, 'mismoApellido':mismoApellido, 'mismaEdad':mismaEdad, 'grupo3MismaEdad':grupo3MismaEdad, 'estudiantes': estudiantes})
    