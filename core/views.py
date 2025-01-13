from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Material, CustomUser, Processo, Rastreabilidade, Falha
from .serializers import UserSerializer, ProcessoSerializer, RastreabilidadeSerializer, FalhaSerializer,  MaterialSerializer
from .permissions import IsAdmin, IsNursing, IsTechnical
from django.http import HttpResponse
import openpyxl
from io import BytesIO
from reportlab.pdfgen import canvas

# ViewSet para o modelo de usuários
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
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
        if CustomUser.objects.filter(email=request.data.get("email")).exists():
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
    

# Endpoint para listar etapas por serial
class RastreabilidadeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serial = request.query_params.get('serial', None)
        if serial:
            rastreabilidade = Rastreabilidade.objects.filter(serial=serial)
        else:
            rastreabilidade = Rastreabilidade.objects.all()
        serializer = RastreabilidadeSerializer(rastreabilidade, many=True)
        return Response(serializer.data)

# Endpoint para relatórios em PDF
class RastreabilidadePDFReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serials = Rastreabilidade.objects.all()
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        pdf.drawString(100, 800, "Relatório de Rastreabilidade")
        y = 750
        for serial in serials:
            pdf.drawString(100, y, f"Serial: {serial.serial} | Etapas: {serial.etapas} | Falhas: {serial.falhas}")
            y -= 20
        pdf.save()
        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/pdf')

# Endpoint para relatórios em XLSX
class RastreabilidadeXLSXReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serials = Rastreabilidade.objects.all()
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Rastreabilidade"
        sheet.append(["Serial", "Etapas", "Falhas"])

        for serial in serials:
            sheet.append([serial.serial, serial.etapas, serial.falhas])

        buffer = BytesIO()
        workbook.save(buffer)
        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
class RastreabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Rastreabilidade.objects.all()
    serializer_class = RastreabilidadeSerializer
    permission_classes = [IsAuthenticated]

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user =CustomUser(email=email).first()
            if user and user.check_password(password):
                attrs['user'] = user
                return attrs
        raise serializers.ValidationError("Credenciais inválidas.")

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer