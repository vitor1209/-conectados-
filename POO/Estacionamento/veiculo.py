# classe PAI
class Veiculo:
    # atributo de classe
    vagas = 20
    if vagas > 20:
        vagas = 20
    elif vagas < 0:
        vagas = 0

    # atributo de instancia
    def __init__(self): 
        self.esta = False
        self.horaEntrada = 0
        self.horaSaida = 0
        
    # nao permitir dados menores que 0
        assert self.horaEntrada >= 0, f"hora Entrada {self.horaEntrada} e menor do que 0"
        assert self.horaSaida >= 0, f"hora Saida {self.horaSaida} e menor do que 0"

    # metodo de classe
    @classmethod
    def ExibirVagas(cls):
        print(f'Tem {cls.vagas} vagas no estacionamento.')

    @classmethod
    def saiu(cls):
        cls.vagas +=1

    @classmethod
    def entrou(cls):
        cls.vagas -=1

    # metodo de classe para as instancias
    def Entrar(self, horaEntrada = 0 ):
        if self.vagas >= 1:
            print(f'O {self.__class__.__name__}, entrou no Estacinamento.')
            __class__.entrou()
            self.esta = True
            self.horaEntrada = horaEntrada
        else:
            print("Sem vagas disponíveis.")

    def sair(self , horaSaida):
        if self.esta == True:
            print(f'O {self.__class__.__name__}, saiu no Estacinamento.')
            __class__.saiu()
            self.horaSaida = horaSaida
            print(f'Você vai pagar {self.pagar() :.2f}R$.')
            self.esta = False
        else:
            print(f'O {self.__class__.__name__}, não esta no Estacinamento.')
    
    def pagar(self):
        if self.horaSaida >= 60:
            horas = self.horaSaida / 60
            return self.valor + (5 * int(horas))
        elif self.horaSaida > 0 & self.horaSaida < 60:
            return self.valor
        else:
             raise ValueError("O valor está errado")