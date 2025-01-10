from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProcessoViewSet, RastreabilidadeViewSet, FalhaViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'processos', ProcessoViewSet)
router.register(r'rastreabilidade', RastreabilidadeViewSet)
router.register(r'falhas', FalhaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Prefixo api/ para todas as rotas
]
