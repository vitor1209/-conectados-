from Comida import comidas
from Comida import perguntasComidas
from Celebridades import celebridades
from Celebridades import perguntasCelebridades
from Videogames import Videogames
from Videogames import perguntasVideogames
import random
import os

class Jogo:
    def __init__(self, nomes, categoria, perguntas):
        self.jogadores = {}
        self.j = 1
        self.categoria = categoria
        self.nomes = nomes
        self.palavra = random.choice(self.categoria)
        self.perguntas = perguntas
        self.impostor = random.choice(self.nomes)

    def part(self):
        for self.nome in self.nomes:
            self.jogadores[self.nome] = 0

    def DividirImpostor(self):
        for pessoa in self.nomes:
            if pessoa == self.impostor:
                print()
                print("Escreva SIM para confirmar")
                pesCerta = str(input(f"Você é {pessoa}? "))
                print()
                if pesCerta == "SIM" or "Sim" or "sim":
                    print(f" Você é o impostor".center(100, '-').upper())
                    input("Aperte Qualquer tecla para continuar ")
                    os.system('cls')
            else :
                print()
                print("Escreva SIM para confirmar")
                pesCerta = str(input(f"Você é {pessoa}? "))
                print()
                if pesCerta == "SIM" or "Sim" or "sim":
                    print(f" A palavra é: {self.palavra} ".center(100, '-').upper())
                    input("Aperte Qualquer tecla para continuar ")
                    os.system('cls')

    def perguntar(self):
        for self.nome in self.nomes:
            print()
            print(f"{self.nome} Pergunta para: {self.nomes[self.j]}".center(100, '-').upper())
            print()
            print(random.choice(self.perguntas))
            print()
            input("Aperte Qualquer tecla para continuar ")
            os.system('cls')
            self.j += 1
            if self.j == len(self.nomes):
                self.j = 0
    
    def votar(self):
     for pessoa in self.nomes:
            os.system('cls')
            print("Votação".center(100, '-').upper())
            print()
            print("Escreva SIM para confirmar")
            pesCerta = str(input(f"Você é {pessoa}? "))
            print()
            if pesCerta == "SIM" or "Sim" or "sim":
               posibilitVoto = []
               for i in self.nomes:
                   if i != pessoa:
                    posibilitVoto.append(i)
            while True:
                    print(f"Você pode votar em: {', '.join(posibilitVoto)}")
                    voto = input(f"Votar em: ").upper()
                    if voto == pessoa:
                        print()
                        print("Você não pode votar em si mesmo")
                        print()
                    elif voto in self.nomes:
                        self.jogadores[voto] += 1
                        break  
                    else:
                        print()
                        print("Nome inválido. Tente novamente.")
                        print()            

    def finalizar(self):
        ListaComidas = []
        ListaComidas.append(self.palavra)
        i = 0
        while i != 3:
            ListaComidas.append(random.choice(self.categoria))
            i += 1
        random.shuffle(ListaComidas)
        maiorVar = max(self.jogadores.values())
        maiorVoto = []
        for chave, valor in self.jogadores.items():
            if valor == maiorVar:
                maiorVoto.append(chave)
        if len(maiorVoto) > 1 : 
            print()
            print("Fim".center(100, '-').upper())
            print()
            print(f'As pessoas com mais votos foram: {", ".join(maiorVoto)}'.center(100, '-').upper())

        else:
            print()
            print("Fim".center(100, '-').upper())
            print()
            print(f'A pessoa com mais votos foi: {", ".join(maiorVoto)}'.center(100, '-').upper())

        print()
        print(f"O Impostor era {self.impostor}".center(100, '-').upper())
        print()
        print(f"{self.impostor} qual palavra era? ".center(100, '-').upper())
        print()
        print(f'Pode ser: {", ".join(ListaComidas)}'.upper())
        print()
        resposta = input("Qual é: ").upper()
        if resposta == self.palavra.upper():
            print()
            print("acertou".upper())
        else :
            print()
            print("não era essa a palavra".upper())

def main():
    nomes = []
    escolha = 0
    os.system('cls')
    print(f" Ache o impostor".center(100, '-').upper())
    print()
    print("Escolha o modo que irá jogar: ")
    print()
    print("1. Comidas")
    print("2. Celebridades")
    print("3. Videogames")
    opcaoJogo = int(input())
    os.system('cls')

    while escolha != 2:
        print("Escolha uma das opções abaixo: ")
        print()
        print("1. Add participante")
        print("2. Começar a jogar")
        escolha = int(input())
        print()
        if escolha == 1:
            nome = str(input("Qual o nome da pessoa: ")).upper()
            nomes.append(nome)
        if escolha == 2:
            if len(nomes) < 3:
                escolha = 0
                print("Só pode jogar com no minimo 3 pessoas") 
            else :
                if opcaoJogo == 1:
                    jogo = Jogo(nomes=nomes, categoria=comidas, perguntas=perguntasComidas)
                    os.system('cls')
                elif opcaoJogo == 2:
                    jogo = Jogo(nomes=nomes, categoria=celebridades, perguntas=perguntasCelebridades)
                    os.system('cls')
                elif opcaoJogo == 3:
                    jogo = Jogo(nomes=nomes, categoria=Videogames, perguntas=perguntasVideogames)
                    os.system('cls')
   
    jogo.part()
    jogo.DividirImpostor()
    jogo.perguntar()
    jogo.votar()
    jogo.finalizar()

if __name__ == '__main__':
    main()