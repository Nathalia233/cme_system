from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone


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


class Material(models.Model):
    # Opções de tipo de material
    TIPO_MATERIAL_CHOICES = [
        ('equipamento', 'Equipamento'),
        ('instrumento', 'Instrumento'),
        ('outro', 'Outro'),
    ]
    
    # Nome do material
    nome = models.CharField(max_length=255)
    # Tipo do material (limitado às escolhas definidas em TIPO_MATERIAL_CHOICES)
    tipo = models.CharField(max_length=50, choices=TIPO_MATERIAL_CHOICES)
    # Data de validade do material
    data_validade = models.DateField()
    # Serial único gerado automaticamente com base no nome do material
    serial = models.CharField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para gerar automaticamente um serial único
        baseado no nome do material caso ainda não tenha sido atribuído.
        """
        if not self.serial:
            # Gera um serial único usando o nome do material e um UUID truncado
            self.serial = f"{self.nome.replace(' ', '_').upper()}_{uuid.uuid4().hex[:6]}"
        # Chama o método save padrão do modelo
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Retorna uma representação em string do material, incluindo nome e tipo.
        """
        return f"{self.nome} - {self.tipo}"

class Etapa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Rastreabilidade(models.Model):
    material = models.ForeignKey('Material', on_delete=models.CASCADE)
    etapa = models.ForeignKey('Etapa', on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=[('Em andamento', 'Em andamento'), ('Finalizado', 'Finalizado')], default='Em andamento')

    def __str__(self):
        return f"Material {self.material.nome} - Etapa {self.etapa.nome}"

    def finalizar(self):
        self.status = 'Finalizado'
        self.data_fim = timezone.now()
        self.save()

    def reiniciar(self):
        """Reinicia o processo para o material."""
        self.status = 'Em andamento'
        self.data_fim = None
        self.save()
        
# Exemplo de função que avança uma etapa para um material
def avancar_etapa(material):
    # Busca a próxima etapa no processo
    etapa_atual = material.etapas.filter(status='Em andamento').first()
    if etapa_atual:
        # Criar uma nova entrada de rastreabilidade
        rastreabilidade = Rastreabilidade.objects.create(
            material=material,
            etapa=etapa_atual
        )
        # Marcar a etapa atual como finalizada
        etapa_atual.finalizar()
        return rastreabilidade
    return None