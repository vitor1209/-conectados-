from rest_framework import generics
from .models import Musica, Avaliacao
from .serializers import MusicaSerializer, AvaliacaoSerializer

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

class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
