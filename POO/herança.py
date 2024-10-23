import random

class personagem():
    def __init__(self , nome):
        self.vida = 100
        self.nome = nome 

class curadeiro(personagem):
    def __init__(self, nome):
        super().__init__(nome)

    def curar(self , cura:personagem):
        cura.vida += 30
        print(f'O {cura.nome} esta com {cura.vida} de HP')

    def dano(self , dano:personagem):
        dano.vida -= random.randint(0, 15)
        print(f'O {dano.nome} esta com {dano.vida} de HP')

class takn(personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.vida = 150

    def dano(self , dano:personagem):
        dano.vida -= random.randint(5, 20)
        print(f'O {dano.nome} esta com {dano.vida} de HP')

    def proteger(self):
        self.vida += random.randint(0, 25)
        print(f'O {self.nome} esta com {self.vida} de HP')

class assasino(personagem):
    def __init__(self, nome ):
        super().__init__(nome)
        self.vida = 85
        self.especialUso = True

    def dano(self , dano:personagem):
        dano.vida -= random.randint(10, 30)
        print(f'O {dano.nome} esta com {dano.vida} de HP')

    def especial(self , dano:personagem):
        if self.especialUso :
            dano.vida -= random.randint(0, 100)
            print(f'O {dano.nome} esta com {dano.vida} de HP')
            self.especialUso = False

class atirado(personagem):
    def __init__(self, nome ):
        super().__init__(nome)
        self.vida = 70
        self.especialUso = True

    def dano(self , dano:personagem):
        dano.vida -= random.randint(0, 30)
        print(f'O {dano.nome} esta com {dano.vida} de HP')
        self.especial = True

    def especial(self , dano:personagem):
        if self.especialUso :
            dano.vida -= random.randint(20, 50)
            self.especialUso = False
            print(f'O {dano.nome} esta com {dano.vida} de HP')

class zoner(personagem):
    def __init__(self, nome ):
        super().__init__(nome)
        self.especialUso = True

    def dano(self , dano:personagem):
        dano.vida -= random.randint(5, 20)
        print(f'O {dano.nome} esta com {dano.vida} de HP')
        self.especial = True
    
    def proteger(self):
        self.vida += random.randint(5, 15)
        print(f'O {self.nome} esta com {self.vida} de HP')
        self.especial = True

    def curar(self , cura:personagem):
        cura.vida += random.randint(5, 15)
        print(f'O {cura.nome} esta com {cura.vida} de HP')
        self.especial = True

    def especial(self , dano:personagem ,  cura:personagem):
        if self.especialUso :
            dano.vida -= random.randint(0, 20)
            self.especialUso = False
            print(f'O {dano.nome} esta com {dano.vida} de HP')
            cura.vida += random.randint(0, 15)
            print(f'O {cura.nome} esta com {cura.vida} de HP')


biron = curadeiro('biron')
leon = assasino('leon')
katrina = zoner('katrina')
hank = takn('hank')

leon.especial(biron)
biron.curar(biron)