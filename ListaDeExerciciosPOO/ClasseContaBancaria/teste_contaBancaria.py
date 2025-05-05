from models.contaBancaria import contaBancaria

class TesteContaBancaria:
    def __init__(self):
        self.conta1 = contaBancaria("Orlando", 900, 800, ["Deposito de 150 reais"])
        self.conta2 = contaBancaria("Ian", 3000, 1000, ["Deposito de 900 reais"])

    def executar_testes(self):
        print(">>> Informações iniciais de Orlando:")
        self.conta1.depositar(150)
        self.conta1.sacar(90)
        self.conta1.transferir(100, self.conta2)

        print("\n>>> Informações iniciais de Ian:")
        self.conta2.depositar(900)
        self.conta2.sacar(570)
        self.conta2.transferir(140, self.conta1)

        print("\n>>> Histórico do Orlando:")    
        self.conta1.exibir_historico()
        print("\n>>> Histórico do Ian:")
        self.conta2.exibir_historico()

        print("\n>>> Saldo do Orlando:")
        self.conta1.exibir_saldo()
        print("\n>>> Saldo do Ian:")
        self.conta2.exibir_saldo()


