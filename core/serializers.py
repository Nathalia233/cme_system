from rest_framework import serializers
from .models import User, Processo, Rastreabilidade, Falha

# Serializer para o modelo de usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

# Serializer para o modelo de processo
class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = ['id', 'nome', 'status', 'data_inicio', 'data_fim']

# Serializer de Rastreabilidade
class RastreabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rastreabilidade
        fields = ['id', 'processo', 'usuario', 'acao', 'data']

# Serializer de Falha
class FalhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Falha
        fields = ['id', 'processo', 'descricao', 'usuario', 'data_ocorrencia']
