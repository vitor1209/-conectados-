from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Musica , Avaliacao
from .serializers import MusicaSerializer , AvaliacaoSerializer

class  MusicaAPIView(APIView):
    def get(self , request ):
        musicas = Musica.objects.all()
        serializer = MusicaSerializer(musicas, many=True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = MusicaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)    



class AvaliacaoAPIView(APIView):
    def get(self , request ):
        Avaliacao  = Musica.objects.all()
        serializer = AvaliacaoSerializer(Avaliacao , many=True)
        return Response(serializer.data)
    def post(self , request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)    