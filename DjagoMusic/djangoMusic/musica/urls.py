from django.urls import path
from .views import MusicaAPIView , AvaliacaoAPIView , AvaliacoesAPIView, MusicasAPIView

urlpatterns = [
    path('musica/<int:pk>', MusicaAPIView.as_view(), name='musica'),
    path('musicas/', MusicasAPIView.as_view(), name='musicas'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
]