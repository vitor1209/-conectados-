class Usuario:
    def __init__(self , nome , email , senha):
        self.nome = nome
        self.__email = email
        self.__senha = senha  

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        # Property atributo somente para a leitura
        return self.__senha

    @senha.setter
    def senha(self, value):
        if len(value) > 10:
            raise Exception("Senha muito longa")
        else:
            self.__senha = value