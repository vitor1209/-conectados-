from django.db import models

class base(models.Model):
    lancamento = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta():
        abstract = True

class Musica(base):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    url = models.URLField(unique=True, max_length=200) #unique=True nao permite criar mais de 1 campo com mesmo nome 
    capa = models.ImageField(upload_to='capas/')

    class Meta():
        verbose_name = "Musica"
        verbose_name_plural = "album"

    def __str__(self):
        return self.titulo
    
class Avaliacao(base):
    LIKE = True
    DISLIKE = False

    VOTE_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike')
    ]


    musica = models.ForeignKey(Musica, related_name='avaliacoes', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comentario = models.TextField(blank=True, default="")
    voto = models.BooleanField(choices=VOTE_CHOICES, default=LIKE)

    @property
    def votoExibi(self):
        return "Like" if self.voto else "Dislike"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"    
        unique_together = ['email', 'musica']

    def __str__(self):
        return f'{self.user} avaliou a musica com um{self.votoExibi}'