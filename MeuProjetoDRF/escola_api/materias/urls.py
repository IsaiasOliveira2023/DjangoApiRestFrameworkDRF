# materias/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MateriaViewSet

router = DefaultRouter()
# Cria automaticamente rotas para GET, POST, PUT, DELETE para /materias/
router.register(r'materias', MateriaViewSet) 

urlpatterns = [
    path("", include(router.urls)),
]