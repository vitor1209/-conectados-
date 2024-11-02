from django.db import models
from django.contrib.auth.models import User

class Enquete(models.Model):
        titulo =  models.CharField(max_length=20)
        descricao =  models.TextField()
        data_inicio = models.DateTimeField()
        data_fim = models.DateTimeField(null=True)

        def __str__(self):
            return self.titulo

class Opcao(models.Model):
        enquete = models.ForeignKey(Enquete, on_delete=models.CASCADE)
        opcao = models.CharField(max_length=20)

        def __str__(self):
            return self.opcao

class Voto(models.Model):
      opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)
      usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
