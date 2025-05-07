import time
  
class contaBancaria:
    '''
    Classe que implementa métodos para manipular uma conta bancária.add()
    Atributos: titular (str), saldo(float), limite (float) e histórico (lista de dicionários)
    
    OBS: Operações no hitórico: 0 - sacar, 1 - depositar, 2 - transferir
    '''
        
    def __init__(self, titular, saldo, limite, historico):
        '''
        Consultador da classe ContaBancaria
        '''
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor):
        '''
        Obejtivo: Metodo que realiza o depósito na conta.
        Entrada: valor (float)
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        if valor >= 0:
            self.saldo += valor
            self.historico.append({"operacao": 0, 
                        "remetente": self.titular,
                        "destinatario": "",
                        "valor": valor,
                        "saldo": self.saldo,
                        "tempo": int(time.time())})
            return True
        else:
            print("Valor inválido")
            return False

    def sacar(self, valor): 
        '''
        Obejtivo: Metodo que realiza o saque na conta.
        Entrada: valor (float)
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": 0, 
                            "remetente": self.titular,
                            "destinatario": "",
                            "valor": valor,
                            "saldo": self.saldo,
                            "tempo": int(time.time())})
            print("Saque realizado com sucesso!")
        else:   # sem plata na conta
            a = input("Deseja utilizar o limite? (R${self.limite}) [s para sim] ")
            if a == "s":
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo e limite insuficientes!")
            else:
                print("Operação com limite cancelada!")
        return False
    
    def transferir(self, valor, destinatario, remetente):
        '''
        Objetivo: Metodo que realiza uma transação.
        Entrada: valor(float)
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        
        
    def exibir_historico(self):
        print("Histórico de Transações:")
        for transacao in self.historico:
            dt = time.localtime(transacao["tempo"])
            print("Operação:", transacao["operacao"], 
                  "- Remetente:", transacao["remetente"], 
                  "- Destinatario:", transacao["destinatario"], 
                  "- Valor:", transacao["valor"], 
                  "- Saldo:", transacao["saldo"], 
                  "- Data e Hora:",  
                  f"{dt.tm_hour}:{dt.tm_min}:{dt.tm_sec} {dt.tm_mday}/{dt.tm_wday}/{dt.tm_year}")
       
    # def exibir_saldo(self): 
