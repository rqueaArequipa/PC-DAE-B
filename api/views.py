from django.shortcuts import render
from rest_framework import viewsets, permissions
from curso.models import Semestre, Curso
from .serializers import SemestreSerializer, CursoSerializer

class SemestreViewSet(viewsets.ModelViewSet):
    queryset = Semestre.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SemestreSerializer
    
class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursoSerializer