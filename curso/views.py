from django.shortcuts import render
from .models import Semestre, Curso

def Index(request):
    list_cursos = Curso.objects.all()
    list_semestres = Semestre.objects.all()
    context = {
        'list_curso': list_cursos,
        'semestre' : list_semestres
    }
    return render(request, 'index.html', context)

def Semestres(request, semestre_id):
    list_cursos = Curso.objects.filter(semestre=semestre_id)
    list_semestres = Semestre.objects.all()
    context = {
        'list_curso': list_cursos,
        'semestre' : list_semestres
    }
    return render(request, 'semestres.html', context)

