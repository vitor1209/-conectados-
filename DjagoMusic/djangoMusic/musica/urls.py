from django.urls import path
from .views import MusicaAPIView , AvaliacaoAPIView

urlpatterns = [
    path('musicas/', MusicaAPIView.as_view(), name='musicas'),
    path('avaliacao/', AvaliacaoAPIView.as_view(), name='avaliacao'),
]