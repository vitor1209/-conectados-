import string, secrets , hashlib , base64 ,os
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken


class FernetHasher :
    letraAleatoria = string.ascii_lowercase + string.ascii_uppercase
    home = Path(__file__).resolve().parent.parent
    ChavePasta = home/'Chaves'

    def __init__(self , chave):
        if not isinstance(chave , bytes):
            chave = chave.encode('utf-8')

        self.fernet = Fernet(chave) 

    @classmethod
    def txtAleatorio(cls , tam=25):
        txt = ''
        for i in range(tam):
            txt += secrets.choice(cls.letraAleatoria)
        return txt
    
    @classmethod
    def CriarChave(cls , arquivar=False):
        valor = cls.txtAleatorio()
        valor = valor.encode('utf-8')
        hasher = hashlib.sha256(valor).digest()
        chave = base64.b64encode(hasher)

        if arquivar:
            return chave, cls.ArquivoChave
        else:
            return chave, None

    @classmethod
    def ArquivoChave(cls , chave):
        if not isinstance(chave , bytes):
            chave = chave.encode('utf-8')

        file = 'Chave.txt'
        while Path(cls.ChavePasta/file).exists():
            file = f'Chave_{cls.txtAleatorio(5)}.txt'

        os.makedirs(cls.ChavePasta, exist_ok=True) 

        with  open(cls.ChavePasta/ file , 'wb') as arq:
            arq.write(chave)

        return  cls.KEY_DIR / file
    
    def encrypt(self , valor):
        if not isinstance(valor , bytes):
            valor = valor.encode('utf-8')

        return self.fernet.encrypt(valor)
    
    def decrypt(self , valor):
        if not isinstance(valor , bytes):
            valor = valor.encode('utf-8')

        try: 
            return self.fernet.decrypt(valor).decode()
        except InvalidToken as e: 
            return 'Token inválido'