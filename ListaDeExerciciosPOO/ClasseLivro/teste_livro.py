from models.livro import livro

class TesteLivro:
    def __init__(self):
        self.livro_teste = livro("O Senhor dos Aneis", "J.R.R Tolkien", 1954, 500, 103)
        self.livro1_teste = livro("Harry Potter e a Pedra Filosofal", " J. K. Rowling", 1997, 208, 23)

    def executar_testes(self):
        print(">>> Informações iniciais do livro:")
        self.livro_teste.exibir_informacoes()
        print("\n>>> Informações iniciais do livro:")
        self.livro1_teste.exibir_informacoes()

        print("\n>>> Avançando de página...")
        self.livro_teste.avancar_pagina()
        self.livro1_teste.avancar_pagina()

        print("\n>>> Informações depois da avançada de página:")
        self.livro_teste.exibir_informacoes()
        print("\n>>> Informações depois da avançada de página:")
        self.livro1_teste.exibir_informacoes()

        print("\n>>> Avançando de página...")
        self.livro_teste.avancar_pagina()
        self.livro1_teste.avancar_pagina()

        print("\n>>> Informações depois da avançada de página:")
        self.livro_teste.exibir_informacoes()
        print("\n>>> Informações depois da avançada de página:")
        self.livro1_teste.exibir_informacoes()

        print("\n>>> Voltando de página...")
        self.livro_teste.voltar_pagina()
        self.livro1_teste.voltar_pagina()

        print("\n>>> Informações depois da volta de página:")
        self.livro_teste.exibir_informacoes()
        print("\n>>> Informações depois da volta de página:")
        self.livro1_teste.exibir_informacoes()