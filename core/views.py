from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Material, User, Processo, Rastreabilidade, Falha
from .serializers import UserSerializer, ProcessoSerializer, RastreabilidadeSerializer, FalhaSerializer,  MaterialSerializer
from .permissions import IsAdmin, IsNursing, IsTechnical

# ViewSet para o modelo de usuários
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def perform_create(self, serializer):
        # Adiciona a lógica de criar o usuário com senha
        password = self.request.data.get('password')
        if not password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
 # Endpoint de cadastro customizado
    def create(self, request, *args, **kwargs):
        # Verifica se o email já existe
        if User.objects.filter(email=request.data.get("email")).exists():
            return Response({"error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Criação do usuário via serializer
        return super().create(request, *args, **kwargs)


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

class MaterialViewSet(viewsets.ModelViewSet):
    
    # Define o queryset que será utilizado para buscar os materiais
    queryset = Material.objects.all()
    # Define o serializer que será usado para a validação e serialização dos dados
    serializer_class = MaterialSerializer
    # Permite apenas usuários autenticados acessarem as rotas deste ViewSet
    permission_classes = [IsAuthenticated]