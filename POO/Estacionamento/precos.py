from veiculo import Veiculo

# classe filhas com um valor unico
class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.valor = 25

class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        self.valor = 11

class Onibus(Veiculo):
    def __init__(self):
        super().__init__()
        self.valor = 50