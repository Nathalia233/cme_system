from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Processo, Rastreabilidade, Falha
from .serializers import UserSerializer, ProcessoSerializer, RastreabilidadeSerializer, FalhaSerializer
from .permissions import IsAdmin, IsNursing, IsTechnical

# ViewSet para o modelo de usuários
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

# ViewSet para o modelo de processos
class ProcessoViewSet(viewsets.ModelViewSet):
    queryset = Processo.objects.all()
    serializer_class = ProcessoSerializer
    permission_classes = [IsAuthenticated]

# ViewSet para o modelo de rastreabilidade
class RastreabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Rastreabilidade.objects.all()
    serializer_class = RastreabilidadeSerializer
    permission_classes = [IsAuthenticated, IsNursing]  # Apenas Enfermagem pode acessar

# ViewSet para o modelo de falhas
class FalhaViewSet(viewsets.ModelViewSet):
    queryset = Falha.objects.all()
    serializer_class = FalhaSerializer
    permission_classes = [IsAuthenticated, IsNursing]  # Apenas Enfermagem pode acessar
