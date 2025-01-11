from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, ProcessoViewSet, RastreabilidadeViewSet, FalhaViewSet, MaterialViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'processos', ProcessoViewSet)
router.register(r'rastreabilidade', RastreabilidadeViewSet)
router.register(r'falhas', FalhaViewSet)
router.register(r'materiais', MaterialViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Registra as rotas dos viewsets
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Registra o token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Registra o refresh do token
]

