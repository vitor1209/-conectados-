from sistema import SistemaDeVotacao

sistema = SistemaDeVotacao()

sistema.registrarUsuario("Alice", "alice@gmail.com", 2525)
sistema.registrarUsuario("joao", "joao@gmail.com" , 4949)

sistema.listarUsuarios()

sistema.criaEnquete("Qual seu sabor de sorvete favorito?", "Escolha seu sabor favorito.", "2/12/2024")

sistema.listarEnquetes()

sistema.enquetes[0].adicionarOpcao("Chocolate")
sistema.enquetes[0].adicionarOpcao("Baunilha")
sistema.enquetes[0].adicionarOpcao("Morango")

sistema.enquetes[0].votar("Chocolate" ,sistema.usuarios[1])
sistema.enquetes[0].votar("Morango",sistema.usuarios[1])

sistema.visualizarResultados(0)