# Generated by Django 5.1.3 on 2024-11-08 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_alter_despesa_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesa',
            name='categoria',
            field=models.CharField(choices=[('Automovel', 'Automóvel'), ('BemEstar', 'Bem Estar'), ('Educacao', 'Educação'), ('Funcionarios', 'Funcionários'), ('Lazer', 'Lazer'), ('Moradia', 'Moradia'), ('Saude', 'Saúde'), ('Seguros', 'Seguros'), ('Transporte', 'Transporte'), ('Vestuario', 'Vestuário'), ('Celular', 'Celular'), ('Investimentos', 'Investimentos'), ('OutrasDespesas', 'Outras Despesas')], default='OutrasDespesas', max_length=30),
        ),
    ]
