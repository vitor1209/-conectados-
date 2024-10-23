class FormaPagamento ():
    def pagar(self): pass

class debito(FormaPagamento):
    def __init__(self , valor , saldo):
        super().__init__()
        self.valor = valor
        self.saldo = saldo
        
    def pagar(self):
        print('Ta no debito e pq tem, (So tem que torcer para o catao passar... )')
        return self.valor - self.saldo 
    
class pix(FormaPagamento):
    def __init__(self , valor , saldo):
        super().__init__()
        self.valor = valor
        self.saldo = saldo

    def pagar(self):
        print('Na hora, mas confere para ver se caiu mesmo')
        return self.valor - self.saldo 
    
class boleto(FormaPagamento):
    def __init__(self , valor , saldo):
        super().__init__()
        self.valor = valor
        self.saldo = saldo

    def pagar(self):
        print('Apos um dias ai...')
        return self.valor - self.saldo 
    
def calculate_preco(FormaPagamento):
    return FormaPagamento.pagar()

debito = debito(450 , 100)
print(calculate_preco(debito))