from django.db import models

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
    categoria = models.CharField(max_length=30, choices=CATEGORIA_CHOICES)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Despesa de R$ {self.valor} em {self.data} ({self.repeticao})"
