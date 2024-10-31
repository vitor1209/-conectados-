from datetime import datetime
from pathlib import Path
import os

class model:
    home = Path(__file__).resolve().parent.parent
    ChavePasta = home / 'db'

    def save(self):
        tabela = Path(self.ChavePasta / f'{self.__class__.__name__}.txt')
        os.makedirs(self.ChavePasta, exist_ok=True) 

        if not tabela.exists():
            tabela.touch()

        with open(tabela, 'a') as arq:           
            arq.write("|".join(list(map(str, self.__dict__.values()))))           
            arq.write('\n')

    @classmethod
    def Get(cls):
        tabela = Path(cls.ChavePasta / f'{cls.__name__}.txt')
        os.makedirs(cls.ChavePasta, exist_ok=True) 

        if not tabela.exists():
            tabela.touch()

        results = []
        atributos = vars(cls()).keys()

        with open(tabela, 'r') as arq: 
            linhas = arq.readlines()  
            
            for linha in linhas:        
                split_v = linha.strip().split('|')        
                tmp_dict = dict(zip(atributos, split_v))        
                results.append(tmp_dict)    

        return results  
             
class Senha(model):
    def __init__(self, dominio=None, senha=False):
        self.dominio = dominio
        self.senha = senha
        self.Criacao = datetime.now().isoformat()  
