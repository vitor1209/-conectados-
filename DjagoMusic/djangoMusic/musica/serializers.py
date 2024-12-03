"""
 serializers são usados para converter dados de modelos Django (ou outros tipos de dados) 
 em formatos que possam ser facilmente convertidos para JSON, XML ou outros formatos de resposta
"""

from rest_framework import serializers
from .models import Musica , Avaliacao

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'  

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'
        extra_kwargs = {
            'email': {'write_only': True}  
        }