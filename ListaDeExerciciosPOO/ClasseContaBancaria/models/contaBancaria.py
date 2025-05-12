import time

class contaBancaria:
    '''
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular (str), saldo(float), limite (float) e histórico (lista de dicionários)
    '''
    def __init__(self, titular, saldo, limite, historico):
        '''
        Consultador da classe ContaBancaria
        '''
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def sacar(self, valor):
        '''
        Obejtivo: Metodo que realiza o saque na conta.
        Entrada: valor (float).
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        if self.saldo >= valor:
            self.saldo -= valor
            self.adiciona_historico("Saque", valor, time.time(), self.saldo)
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        '''
        Obejtivo: Metodo que realiza o depósito na conta.
        Entrada: valor (float).
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        self.saldo += valor
        self.adiciona_historico("Depósito", valor, time.time(), self.saldo)
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    def transferir(self, valor, destino):
        '''
        Objetivo: Metodo que realiza uma transação.
        Entrada: valor (float) e obj contaBancaria
        Return: Se o ok -> True, Se o NOK -> False.
        '''
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.adiciona_historico("Transferência Enviada", valor, time.time(), self.saldo, destino.titular)
            destino.adiciona_historico("Transferência Recebida", valor, time.time(), destino.saldo, self.titular)
            print(f"Transferência de R${valor:.2f} para {destino.titular} realizada com sucesso!")
        else:
            print("Saldo insuficiente para transferir.")

    def adiciona_historico(self, tipo, valor, timestamp, saldo_pos, conta_destino=None):
        data_hora = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(timestamp))
        if conta_destino:
            descricao = f"{tipo} de R${valor:.2f} {'para' if 'Enviada' in tipo else 'de'} {conta_destino}"
        else:
            descricao = f"{tipo} de R${valor:.2f}"
        self.historico.append(f"{data_hora} - {descricao} | Saldo após operação: R${saldo_pos:.2f}")

    def exibir_historico(self):
        print(f"\nHistórico de {self.titular}:")
        if self.historico:
            for linha in self.historico:
                print(linha)
        else:
            print("Nenhuma transação realizada.")
