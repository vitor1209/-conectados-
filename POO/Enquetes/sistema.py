from usuario import Usuario
from enquete import Enquete
from datetime import datetime

data_atual = datetime.now()
dia_atual = data_atual.date()

class SistemaDeVotacao():
    def __init__(self):
        self.usuarios = []
        self.enquetes = []

    def criaEnquete(self , titulo , descricao ,data_fim , data_inicio = dia_atual):
        novaEnquete = Enquete(titulo, descricao, data_inicio, data_fim)
        self.enquetes.append(novaEnquete)
        print('Enquete Registrada com sucesso')

    def listarEnquetes(self):
        print("Enquetes disponíveis:")
        for enquete in (self.enquetes):
            print(f"{enquete.titulo} (Início: {enquete.data_inicio}, e o fim: {enquete.data_fim})")

    def visualizarResultados(self , enquete:Enquete):
        print("Resultados:")
        for enquete in (self.enquetes):
            print(f'O resultado da Enquete {enquete.titulo}, foi {enquete.votos}')

    def registrarUsuario(self,  nome , email , senha):
        novoUsuario= Usuario(nome , email , senha)
        self.usuarios.append(novoUsuario)
        print('Usuario com sucesso')

    def listarUsuarios(self):
        print("Usuários registrados:")
        for usuario in self.usuarios:
            print(f"{usuario.nome} ({usuario.email})")