from usuario import Usuario
from datetime import datetime

data_atual = datetime.now()
dia_atual = data_atual.date()

class Enquete:
    def __init__(self , titulo , descricao ,data_fim , data_inicio = dia_atual):
        self.titulo = titulo
        self.descricao = descricao
        self.data_fim = data_fim
        self.data_inicio = data_inicio
        self.opcoes = []  
        self.votos = {} 


    def adicionarOpcao(self , opcao):
        if opcao not in self.opcoes:
            self.opcoes.append(str(opcao))
            self.votos[opcao] = 0 
            print(f"A opção {opcao}, foi adicionada com sucesso")
        else:
            print(f"A opção {opcao}, ja existe")

    def votar(self , opcao , pessoa:Usuario):
        if opcao in self.opcoes:
            self.votos[opcao] += 1
            print(f'Seu voto foi registrado com sucesso, {pessoa.nome}')
        else:
            print(f'Essa opção não existe')

    def resultados(self):
        print(f'O resultado da Enquete {self.titulo}, foi {self.votos}')
    
    def VerOpcoes(self):
        print("As opções são:")
        for opcao in self.votos:
            print(opcao)