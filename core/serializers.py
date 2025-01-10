from rest_framework import serializers # type: ignore
from .models import User, Processo

# Serializer para o modelo de usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

# Serializer para o modelo de processo
class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = ['id', 'nome', 'status', 'data_inicio', 'data_fim']