class contaBancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor): #Adiciona um valor ao saldo da conta.
        self.saldo += valor
        self.historico.append(f"Deposito de {valor} reais")

    def sacar(self, valor): #Subtrai um valor do saldo da conta.
        if self.saldo - valor >= self.limite:
            self.saldo -= valor
            self.historico.append(f"Saque de {valor} reais")
        else:
            print("Limite insuficiente")
 
    def transferir(self, valor, conta_destino): # Transfere um valor para outra conta bancária.
        conta_destino.depositar(valor)
        self.historico.append(f"Transferencia de {valor} reais para {conta_destino.titular}")

    def exibir_historico(self): # Exibe todas as transações realizadas na conta.
        for transacao in self.historico:
            print(transacao)

    def exibir_saldo(self): # Exibe o saldo atual da conta, incluindo o limite disponível.
        print(f"Saldo atual: {self.saldo} reais")