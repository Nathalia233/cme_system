from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Processo
from .serializers import UserSerializer, ProcessoSerializer

# ViewSet para o modelo de usuários
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Definir senha com hash
        password = self.request.data.get('password')
        user = serializer.save()
        user.set_password(password)
        user.save()

# ViewSet para o modelo de processos
class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer
    permission_classes = [IsAuthenticated]
    