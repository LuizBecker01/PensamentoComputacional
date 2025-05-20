from models.filme import filme

class TesteFilme:
    def __init__(self):
        # Criando um objeto do tipo Filme com valores iniciais
        self.filme_teste = filme("Até O Último Homem", "Guerra/Drama", 139, 9.0)
        self.filme1_teste = filme("Smile", "terror", 115, 8.5)

    def executar_testes(self):
        print(">>> Informações iniciais do filme:")
        self.filme_teste.exibir_informacoes()
        print("\n>>> Informações iniciais do filme:")
        self.filme1_teste.exibir_informacoes()

        print("\n>>> Alterando avaliação...")
        self.filme_teste.avaliar(10.0)
        self.filme1_teste.avaliar(9.2)

        print("\n>>> Informações após nova avaliação:")
        self.filme_teste.exibir_informacoes()
        print("\n>>> Informações após nova avaliação:")
        self.filme1_teste.exibir_informacoes()