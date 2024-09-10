from Comida import comidas
from Comida import perguntasComidas
from Celebridades import celebridades
from Celebridades import perguntasCelebridades
from Videogames import Videogames
from Videogames import perguntasVideogames
import random
import os

class JogoComidas():
    def __init__(self, nomes):
        self.jogadores = {}
        self.j = 1
        self.comidas = comidas
        self.nomes = nomes
        self.comida = random.choice(self.comidas)
        self.perguntas = perguntasComidas
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
                    print(f" A comida é: {self.comida} ".center(100, '-').upper())
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
        ListaComidas.append(self.comida)
        i = 0
        while i != 3:
            ListaComidas.append(random.choice(self.comidas))
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
        print(f"{self.impostor} qual comida era? ".center(100, '-').upper())
        print()
        print(f'Pode ser: {", ".join(ListaComidas)}'.upper())
        print()
        resposta = input("Qual é: ").upper()
        if resposta == self.comida.upper():
            print()
            print("acertou".upper())
        else :
            print()
            print("não era essa a comida".upper())

class JogoCelebridades():
    def __init__(self, nomes):
        self.jogadores = {}
        self.j = 1
        self.celebridades = celebridades
        self.nomes = nomes
        self.celebridade = random.choice(self.celebridades)
        self.perguntas = perguntasCelebridades
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
                    print(f" A celebridade é: {self.celebridade} ".center(100, '-').upper())
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
                    elif voto in posibilitVoto:
                        self.jogadores[voto] += 1
                        break  
                    else:
                        print()
                        print("Nome inválido. Tente novamente.")
                        print()
                
    def finalizar(self):
        ListaCelebridades = []
        ListaCelebridades.append(self.celebridade)
        i = 0
        while i != 3:
            ListaCelebridades.append(random.choice(self.celebridades))
            i += 1
        random.shuffle(ListaCelebridades)
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
        print("Qual celebridade era? ".center(100, '-').upper)
        print()
        print(f'Pode ser: {", ".join(ListaCelebridades)}'.upper)

        resposta = input("Qual é: ").upper
        if resposta == self.celebridade.upper():
            print()
            print("acertou".upper())
        else :
            print()
            print("não era essa a celebridade".upper())

class JogoVideogames():
    def __init__(self, nomes):
        self.jogadores = {}
        self.j = 1
        self.Videogames = Videogames
        self.nomes = nomes
        self.Videogame = random.choice(self.Videogames)
        self.perguntas = perguntasVideogames
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
                    print(f" O jogo é: {self.Videogame} ".center(100, '-').upper())
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
                    elif voto in posibilitVoto:
                        self.jogadores[voto] += 1
                        break  
                    else:
                        print()
                        print("Nome inválido. Tente novamente.")
                        print()
                
    def finalizar(self):
        ListaVideogames = []
        ListaVideogames.append(self.Videogame)
        i = 0
        while i != 3:
            ListaVideogames.append(random.choice(self.Videogames))
            i += 1
        random.shuffle(ListaVideogames)
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
        print(f"{self.impostor} qual jogo era? ".center(100, '-').upper())
        print()
        print(f'Pode ser: {", ".join(ListaVideogames)}'.upper())
        print()
        resposta = input("Qual é: ").upper()
        if resposta == self.Videogame.upper():
            print()
            print("acertou".upper())
        else :
            print()
            print("não era esse o jogo".upper())

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
                    jogo = JogoComidas(nomes)
                    os.system('cls')
                if opcaoJogo == 2:
                    jogo = JogoCelebridades(nomes)
                    os.system('cls')
                if opcaoJogo == 3:
                    jogo = JogoVideogames(nomes)
                    os.system('cls')
   
    jogo.part()
    jogo.DividirImpostor()
    jogo.perguntar()
    jogo.votar()
    jogo.finalizar()

if __name__ == '__main__':
    main()