from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuário Customizado
class User(AbstractUser):
    TECHNICAL = 'Técnico'
    NURSING = 'Enfermagem'
    ADMINISTRATIVE = 'Administrativo'
    ROLE_CHOICES = [
        (TECHNICAL, 'Técnico'),
        (NURSING, 'Enfermagem'),
        (ADMINISTRATIVE, 'Administrativo'),
    ]
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=TECHNICAL
    )

    # Define o campo a ser usado para autenticação
    USERNAME_FIELD = 'email'

    # Define quais campos são obrigatórios ao criar o usuário
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']  # Não inclui 'email' porque já está em USERNAME_FIELD

    # Tornando o email único
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

# Modelo de Processo
class Processo(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="pendente")
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome

# Modelo de Rastreabilidade
class Rastreabilidade(models.Model):
    processo = models.ForeignKey(Processo, related_name='rastreabilidade', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    acao = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rastreabilidade do processo {self.processo.nome} por {self.usuario.username}"

# Modelo de Falha
class Falha(models.Model):
    processo = models.ForeignKey(Processo, related_name='falhas', on_delete=models.CASCADE)
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_ocorrencia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Falha no processo {self.processo.nome} reportada por {self.usuario.username}"
