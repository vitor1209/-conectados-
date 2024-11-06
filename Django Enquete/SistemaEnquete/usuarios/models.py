from django.db import models
from django.contrib.auth.models import User

class Enquete(models.Model):
        titulo =  models.CharField(max_length=20)
        descricao =  models.TextField()
        data_inicio = models.DateTimeField()
        data_fim = models.DateTimeField(null=True)

        def __str__(self):
            return self.titulo
        
        def VotosTotais(self):
              votos = Opcao.objects.filter(enquete=self).aggregate(
                    total_votos=models.Sum('votos')
                    )

              return votos['total_votos'] or 0
        
        def resultados(self):
                totalVotos = self.VotosTotais()
                votos = []
                for opcao in self.opcoes.all():
                    percentual = 0
                    if opcao.votos > 0 and totalVotos > 0:
                        percentual = opcao.votos / totalVotos * 100
                    votos.append(
                          {
                                'txt': Opcao.opcao,
                                'votos': Opcao.votos,
                                'percentual': round(percentual , 2)
                          }
                    )
                
                return votos

    

class Opcao(models.Model):
        enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE,  related_name='opcoes')
        opcao = models.CharField(max_length=20)
        votos = models.IntegerField(default=0)

        def __str__(self):
            return self.opcao  