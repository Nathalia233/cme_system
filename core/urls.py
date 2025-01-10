from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import UserViewSet, ProcessoViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'processos', ProcessoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]