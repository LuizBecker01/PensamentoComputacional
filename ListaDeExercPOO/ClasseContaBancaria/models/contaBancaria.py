import time

class ContaBancaria:
    '''
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular (str), saldo(float), limite (float) e histórico (lista de dicionários)
    '''
    def __init__(self, titular, saldo, limite, historico, chave_pix):
        '''
        Consultador da classe ContaBancaria
        '''
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__chave_pix = chave_pix
        self.__historico = historico

    def sacar(self, valor):
        '''
        Obejtivo: Metodo que realiza o saque na conta.
        Entrada: valor (float).
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        if valor <= 0:
            print("Valor inválido.")
            return False

        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__adiciona_historico("Saque", valor, time.time(), self.__saldo)
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True

        elif valor <= self.__saldo + self.__limite:
            print("Saldo insuficiente. Deseja usar o limite para completar a operação? (s/n)")
            escolha = input().strip().lower()
            if escolha == "s":
                self.__saldo -= valor
                self.__adiciona_historico("Saque com limite", valor, time.time(), self.__saldo)
                print(f"Saque de R${valor:.2f} realizado usando o limite.")
                return True
            else:
                print("Operação cancelada pelo usuário.")
                return False

        else:
            print("Saldo e limite insuficientes.")
            return False

    def depositar(self, valor):
        '''
        Obejtivo: Metodo que realiza o depósito na conta.
        Entrada: valor (float).
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        self.__saldo += valor
        self.__adiciona_historico("Depósito", valor, time.time(), self.__saldo)
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")

    def pix(self, chave_pix_destino, valor, contas):
        '''
        Realiza transferência via Pix para outra conta usando a chave Pix.
        '''
        if valor <= 0:
            print("Valor inválido.")
            return False
        
        destino = None
        for conta in contas:
            if conta.get_chave_pix() == chave_pix_destino:
                destino = conta
                break

        if not destino:
            print("Conta de destino não encontrada.")
            return False

        if valor <= self.__saldo:
            self.__saldo -= valor
        elif valor <= self.__saldo + self.__limite:
            print("Saldo insuficiente. Deseja usar o limite para completar o Pix? (s/n)")
            escolha = input().strip().lower()
            if escolha == "s":
                self.__saldo -= valor
                print("Pix realizado usando o limite.")
            else:
                print("Operação cancelada pelo usuário.")
                return False
        else:
            print("Saldo e limite insuficientes.")
            return False
        
        destino.__saldo += valor
        timestamp = time.time()
        self.__adiciona_historico("Pix Enviado", valor, timestamp, self.__saldo, destino.__titular)
        destino.__adiciona_historico("Pix Recebido", valor, timestamp, destino.__saldo, self.__titular)
        return True

    def transferir(self, valor, destino):
        '''
        Objetivo: Metodo que realiza uma transação.
        Entrada: valor (float), destino (obj ContaBancaria).
        Return: Se ok -> True, Se não ok -> False.
        '''
        if valor <= 0:
            print("Valor inválido.")
            return False

        if valor <= self.__saldo:
            self.__saldo -= valor
        elif valor <= self.__saldo + self.__limite:
            print("Saldo insuficiente. Deseja usar o limite para completar a transferência? (s/n)")
            escolha = input().strip().lower()
            if escolha == "s":
                self.__saldo -= valor
                print("Transferência realizada usando o limite.")
            else:
                print("Operação cancelada pelo usuário.")
                return False
        else:
            print("Saldo e limite insuficientes.")
            return False

        destino.__saldo += valor
        timestamp = time.time()
        self.__adiciona_historico("Transferência enviada", valor, timestamp, self.__saldo, destino.__titular)
        destino.__adiciona_historico("Transferência recebida", valor, timestamp, destino.__saldo, self.__titular)
        return True

    def __adiciona_historico(self, tipo, valor, timestamp, saldo_pos, conta_destino=None):
        data_hora = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(timestamp))
        if conta_destino:
            descricao = f"{tipo} de R${valor:.2f} {'para' if 'Enviada' in tipo else 'de'} {conta_destino}"
        else:
            descricao = f"{tipo} de R${valor:.2f}"
        self.__historico.append(f"{data_hora} - {descricao} | Saldo após operação: R${saldo_pos:.2f}")

    def exibir_historico(self):
        print(f"\nHistórico de {self.__titular}:")
        if self.__historico:
            for linha in self.__historico:
                print(linha)
        else:
            print("Nenhuma transação realizada.")

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def get_chave_pix(self):
        return self.__chave_pix

    @property
    def historico(self):
        return self.__historico