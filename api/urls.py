from rest_framework.routers import DefaultRouter
from .views import SemestreViewSet, CursoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('semestres', SemestreViewSet, 'semestres')
router.register('curso', CursoViewSet, 'curso')

urlpatterns = [
    path('',include(router.urls)),
]