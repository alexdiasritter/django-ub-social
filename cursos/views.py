from rest_framework import generics 
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

class CursosAPIView(generics.ListCreateAPIView):
    
    queryset: list[Curso] = Curso.objects.all()
    serializer_class: CursoSerializer = CursoSerializer

class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset: list[Curso] = Curso.objects.all()
    serializer_class: CursoSerializer = CursoSerializer
    
    

class AvaliacoesAPIView(generics.ListCreateAPIView):
    
    queryset: list[Avaliacao] = Avaliacao.objects.all()
    serializer_class: AvaliacaoSerializer = AvaliacaoSerializer
    
class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):

    
    queryset: list[Avaliacao] = Avaliacao.objects.all()
    serializer_class: AvaliacaoSerializer = AvaliacaoSerializer