from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def crearDocente(request):
    return render(request, 'crearDocente.html')

def listarDocentes(request):
    return render(request, 'listarDocentes.html')

def crearCurso(request):
    return render(request, 'crearCurso.html')

def listarCursos(request):
    return render(request, 'listarCursos.html')