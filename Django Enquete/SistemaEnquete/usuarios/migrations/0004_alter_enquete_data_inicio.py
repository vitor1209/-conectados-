# Generated by Django 5.1.2 on 2024-10-27 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquete',
            name='data_inicio',
            field=models.DateTimeField(),
        ),
    ]
