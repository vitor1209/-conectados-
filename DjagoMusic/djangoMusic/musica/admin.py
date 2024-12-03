from django.contrib import admin
from .models import Musica , Avaliacao

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ['titulo','artista','url','capa']

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['musica','user','email','comentario','voto']