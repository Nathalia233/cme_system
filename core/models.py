from django.db import models
from django.contrib.auth.models import AbstractUser

# Definindo o modelo de usuário
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

    def __str__(self):
        return self.username

# Modelo de Processo
class Processo(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="pendente")
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome