class contaBancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor): #Adiciona um valor ao saldo da conta.
        if valor >= 0:
            self.saldo += valor
        else:
            print("Valor inválido")

    def sacar(self, valor): #Subtrai um valor do saldo da conta.
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque de R${valor}")
            print("Saque realizado com sucesso!")
        else:
            a = input("Deseja utilizar o limite? (R${self.limite}) [s/n] ")
            if a == "s":
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo e limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
 
    def transferir(self): # Transfere um valor para outra conta bancária.


    def exibir_historico(self): # Exibe todas as transações realizadas na conta.
       

    def exibir_saldo(self): # Exibe o saldo atual da conta, incluindo o limite disponível.
       