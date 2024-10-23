class Biblioteca:
    totalLivros = 0  

    def __init__(self, titulo, autor, ano_lancamento):
        self.titulo = titulo
        self.autor = autor
        self.ano_lancamento = ano_lancamento
        self.emprestado = False
        Biblioteca.totalLivros += 1 

    def emprestar(self):
        if self.emprestado == False:
            print(f'O livro {self.titulo}, foi emprestado')
            self.emprestado = True
            print()
        else:
            print(f'O livro {self.titulo}, ja está emprestado')
            print()

    def devolver(self):
        if self.emprestado == True:
            print(f'O livro {self.titulo}, será devolvido')
            self.emprestado = False
            print()
        else:
             print(f'O livro {self.titulo}, ja esta na biblioteca')
             print()

    @classmethod  # acesso apartir da probria classe  para acessar atributos de classe 
    def Livros(cls):
        return cls.totalLivros
    
livro1 = Biblioteca("O Pássaro Contra a Vidraça" , "Giselda Laporta Nicolelis" , '1981')
livro2 = Biblioteca("Os Lusíadas", "Luís de Camões", '1556')

livro1.devolver()
livro1.emprestar()
livro2.emprestar()
livro2.devolver()
print(f'A biblioteca tem, {Biblioteca.Livros()}, cadastrados')