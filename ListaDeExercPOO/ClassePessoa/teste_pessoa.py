from models.pessoa import pessoa

class TestePessoa:
    def __init__(self):
        self.pessoa_teste = pessoa("Mauro", 25, 1.70)
        self.pessoa1_teste = pessoa("Joaquim", 20, 1.81)
        self.pessoa2_teste = pessoa("Ian", 18, 1.77)

    def executar_testes(self):
        print(">>> Informações iniciais:")
        self.pessoa_teste.exibir_informacoes()
        print(">>> Informações iniciais:")
        self.pessoa1_teste.exibir_informacoes()
        print(">>> Informações iniciais:")
        self.pessoa2_teste.exibir_informacoes()

        print("\n>>> Aniversario...")
        self.pessoa_teste.aniversario()
        self.pessoa1_teste.aniversario()
        self.pessoa2_teste.aniversario()

        print("\n>>> Crescer...")
        self.pessoa_teste.crescer(0.05)
        self.pessoa1_teste.crescer(0.02)
        self.pessoa2_teste.crescer(0.10)

        print("\n>>> Informações depois do aniversário e crescimento:")
        self.pessoa_teste.exibir_informacoes()
        print("\n>>> Informações depois do aniversário e crescimento:")
        self.pessoa1_teste.exibir_informacoes()
        print("\n>>> Informações depois do aniversário e crescimento:")
        self.pessoa2_teste.exibir_informacoes()