from django.db import models
from django.contrib.auth.models import User

class Despesa(models.Model):
    VALOR_CHOICES = [
        ('Unica', 'Única'),
        ('Parcelada', 'Parcelada'),
        ('Fixa', 'Fixa'),
    ]

    CATEGORIA_CHOICES = [
        ('Automovel', 'Automóvel'),
        ('BemEstar', 'Bem Estar'),
        ('Educacao', 'Educação'),
        ('Funcionarios', 'Funcionários'),
        ('Lazer', 'Lazer'),
        ('Moradia', 'Moradia'),
        ('Saude', 'Saúde'),
        ('Seguros', 'Seguros'),
        ('Transporte', 'Transporte'),
        ('Vestuario', 'Vestuário'),
        ('Celular', 'Celular'),
        ('Investimentos', 'Investimentos'),
        ('OutrasDespesas', 'Outras Despesas'),
    ]
    
    valor = models.DecimalField(max_digits=100000, decimal_places=2,)
    data = models.DateField()
    repeticao = models.CharField(max_length=10, choices=VALOR_CHOICES, default='Unica')
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES, default='OutrasDespesas')
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Despesa de R$ {self.valor} em {self.data} ({self.repeticao})"
