import sys 
import os 
sys.path.append(os.path.abspath(os.curdir))

from model.senhas import Senha
from views.senha import FernetHasher

acao = input('Digite 1 para salvar uma nova senha ou 2 para ver uma determinada senha: ')

if acao == '1':  
    if len(Senha.Get()) == 0:
        Chave, path = FernetHasher.CriarChave(arquivar=True)
        print('Sua chave foi criada, salve-a com cuidado. Caso a perca, não poderá recuperar suas senhas.')
        
        print(f'Chave: {Chave.decode("utf-8")}')
        
        if path:
            print('Chave salva no arquivo. Lembre-se de remover o arquivo após transferi-la para um local seguro')
            print(f'Caminho: {path}')
        
        dominio = input('Domínio: ')
        senha = input('Senha: ')
        fernet_user = FernetHasher(Chave)
        
        p1 = Senha(dominio, fernet_user.encrypt(senha.encode('utf-8')).decode('utf-8'))
        p1.save()
    else:
        key = input('Digite sua chave usada para criptografia. Use sempre a mesma chave: ')

elif acao == '2':
    dominio = input('Domínio: ')
    Chave = input('Chave: ').encode('utf-8') 
    fernet_user = FernetHasher(Chave)
    data = Senha.Get()  

    senha = None  
    for i in data:
        if dominio in i['dominio']:
            senha = fernet_user.decrypt(i['senha'].encode('utf-8'))
            break  
    if senha:
        print(f'Sua senha: {senha}')            
    else:
        print('Nenhuma senha encontrada para esse domínio.')