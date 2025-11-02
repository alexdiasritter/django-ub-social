from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk: str=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacao.all, many=False)
        return Response(serializer.data)

'''
    class AvaliacaoViewSet (viewsets.ModelViewSet):
        queryset = Avaliacao.objects.all()
        serializer_class = AvaliacaoSerializer
'''

class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer