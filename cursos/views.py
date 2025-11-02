from rest_framework import generics 
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

class CursosAPIView(generics.ListCreateAPIView):
    
    queryset: list[Curso] = Curso.objects.all()
    serializer_class: CursoSerializer = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset: list[Curso] = Curso.objects.all()
    serializer_class: CursoSerializer = CursoSerializer
    
    

class AvaliacoesAPIView(generics.ListCreateAPIView):
    
    queryset: list[Avaliacao] = Avaliacao.objects.all()
    serializer_class: AvaliacaoSerializer = AvaliacaoSerializer
    
    def get_queryset(seld):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset: list[Avaliacao] = Avaliacao.objects.all()
    serializer_class: AvaliacaoSerializer = AvaliacaoSerializer
    
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))