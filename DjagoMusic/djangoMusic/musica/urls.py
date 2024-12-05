from django.urls import path
from .views import MusicaAPIView , AvaliacaoAPIView , AvaliacoesAPIView, MusicasAPIView, MusicaViewSet,AvaliacaoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('misicas', MusicaViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('musica/<int:pk>', MusicaAPIView.as_view(), name='musica'),
    path('musica/<int:musica_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='musicaAvaliacao'),
    path('musica/<int:musica_pk>/avaliacoes/<int:avaliacao_pk>', MusicaAPIView.as_view(), name='musica_Avaliacao'),
    path('musicas/', MusicasAPIView.as_view(), name='musicas'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
]