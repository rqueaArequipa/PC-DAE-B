from django.db import models

class Semestre(models.Model):
    nombre = models.CharField(max_length=200)
    pud_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo