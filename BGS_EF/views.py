from django.shortcuts import render, redirect
from BGS_EF.forms import FormDocente, FormCurso
from BGS_EF.models import Docente, Curso

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def integrantes(request):
    return render(request, 'integrantes.html')

def crearDocente(request):
    formulario = FormDocente()
    return render(request, 'crearDocente.html',{
        'form': formulario
    })

def guardarDocente(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    apellido_paterno = request.POST['apellido_paterno']
    apellido_materno = request.POST['apellido_materno']
    dni = request.POST['dni']
    Fecha_nacimiento = request.POST['Fecha_nacimiento']
    estado = request.POST['estado']

    docente = Docente(
        codigo = codigo,
        nombre = nombre,
        apellido_paterno = apellido_paterno,
        apellido_materno = apellido_materno,
        dni = dni,
        Fecha_nacimiento = Fecha_nacimiento,
        estado = estado
    )

    docente.save()
    return redirect('listarDocentes')

def eliminarDocente(request, id):
    docente = Docente.objects.get(pk=id)
    docente.delete()
    return redirect('listarDocentes')


def listarDocentes(request):
    docentes = Docente.objects.all()
    return render(request, 'listarDocentes.html',{
        'docentes' : docentes
    })

def crearCurso(request):
    formulario = FormCurso()
    return render(request, 'crearCurso.html', {
        'form':formulario
    })

def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listarCursos.html', {
        'cursos':cursos
    })

def guardarCurso(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    horas = request.POST['horas']
    creditos = request.POST['creditos']
    estado = request.POST['estado']

    curso = Curso(
        codigo = codigo,
        nombre = nombre,
        horas = horas,
        creditos = creditos,
        estado = estado
    )
    curso.save()
    return redirect('listarCursos')

def eliminarCurso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('listarCursos')
