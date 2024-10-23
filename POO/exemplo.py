class lampada():  # clase
    def __init__(self , cor , brilho):
        # Propriedades/atributos 
        self.cor = cor 
        self.brilho = brilho
        self.acessa = False

    # Métodos
    def acender(self):
        if self.acessa:
            print(f'A lampada {self.cor} já esta acessa')
        else:
            print(f'A luz de cor {self.cor} brilha a {self.brilho}')
            self.acessa = True

    def apagar(self):
        if self.acessa:
            print(f'A lampada de cor {self.cor}, será apagada')
            self.acessa = False
        else:
            print(f'A luz de cor {self.cor} já esta apagada.')

# Objetos
lampada1 = lampada('branca' , 120)
# Objetos
lampada2 = lampada('vermelha' , 40)
# Objetos
lampada3 = lampada('verde' , 70)

lampada1.acender()
lampada1.acender()
lampada2.acender()
lampada3.apagar()
lampada1.apagar()
lampada3.acender()