from rest_framework import serializers
from .models import User, Processo, Rastreabilidade, Falha, Material

# Serializer para o modelo de usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


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


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        # Define os campos que serão serializados
        fields = ['id', 'nome', 'tipo', 'data_validade', 'serial']
        
