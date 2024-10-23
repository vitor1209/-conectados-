'''Cada aluno tem uma lista de notas em diferentes disciplinas, e o professor pode adicionar ou consultar 
essas notas. No entanto, é importante garantir que as notas adicionadas estejam dentro de um intervalo 
válido (por exemplo, de 0 a 10) e que o aluno ou terceiros não possam modificar diretamente as notas sem 
passar pelo sistema de regras.'''

class NSA():
    def __init__(self):
        self.__notas  = []

    def AddNota(self , *notas):
            for nota in notas : 
                if 0 <= nota <= 10:
                    self.__notas.append(nota)
                else:
                    print(f'A nota {nota} e de um valor invalido preencha com um numero de 0 a 10')

    def MostraNota(self):
        return self.__notas
    
meuNSA = NSA()

meuNSA.AddNota(8 , 7 , 9.3 , 22)

print(meuNSA.MostraNota())

class NSA():
    def __init__(self):
        self.notas  = []

    def AddNota(self , *notas):
            for nota in notas : 
                if 0 <= nota <= 10:
                    self.notas.append(nota)
                else:
                    print(f'A nota {nota} e de um valor invalido preencha com um numero de 0 a 10')

    def MostraNota(self):
        return self.notas
    
meuNSA = NSA()
lista = [45 , 10 , 1000 , 10 , "E TI HAHA E TI HAHAHA"]
meuNSA.notas.extend(lista)

print(meuNSA.MostraNota())