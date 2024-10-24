from usuario import Usuario
from enquete import Enquete

user1 = Usuario("Alice", "alice@gmail.com", 2525)
user2 = Usuario("joao", "joao@gmail.com" , 4949)

enquet = Enquete("Qual seu sabor de sorvete favorito?", "Escolha seu sabor favorito.", "2/12/2024")

enquet.adicionarOpcao("Chocolate")
enquet.adicionarOpcao("Baunilha")
enquet.adicionarOpcao("Morango")
enquet.adicionarOpcao("Chocolate")

enquet.VerOpcoes()

enquet.votar("Baunilha" , user1)
enquet.votar("Baunilha" , user2)

enquet.resultados()
