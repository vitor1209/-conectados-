from rest_framework import generics
from .models import Musica, Avaliacao
from .serializers import MusicaSerializer, AvaliacaoSerializer
from rest_framework import viewsets , mixins
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

#  listar todas as musicas ou criar uma nova
class MusicasAPIView(generics.ListCreateAPIView): # C = create
    queryset = Musica.objects.all()
    # Especifica o serializer q vai por converter os dados entre JSON e o modelo
    serializer_class = MusicaSerializer

# Classe para operações específicas em uma música (detalhar (R), atualizar (U) ou excluir (D))
class MusicaAPIView(generics.RetrieveUpdateDestroyAPIView):
    # tem q devinir a música específica pelo ID
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer

class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('musica_pk'):
            return self.queryset.filter(musica_id = self.kwargs.get('musica_pk'))
        return self.queryset.all()

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('musica_pk'):
            return get_object_or_404(self.get_queryset(), musica_id = self.kwargs.get('musica_pk'), pk = self.kwargs.get('avaliacao_pk') )
        return get_object_or_404(self.get_queryset(), pk = self.kwargs.get('avaliacao_pk')  )
    

############################ API versão 2

class MusicaViewSet(viewsets.ModelViewSet):
    queryset =  Musica.objects.all()
    serializer_class = MusicaSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        musica = self.get_object()
        serializer = AvaliacaoSerializer(musica.avaliacoes.all(), many=True)
        return Response(serializer.data)

'''  PADRAO
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    '''

class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer