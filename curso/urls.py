from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index, name='index'),
    path('semestre/<int:semestre_id>/', views.Semestres, name='semestre')
]