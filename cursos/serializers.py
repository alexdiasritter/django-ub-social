from rest_framework import serializers # type: ignore
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Avaliacao
        fields = ['id', 'curso', 'nome', 'email', 'comentario', 'avaliacao', 'criacao', 'atualizacao', 'ativo']

class CursoSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'url', 'criacao', 'atualizacao', 'ativo', 'avaliacoes']