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

    def depositar(self, valor, remetente = None):
        '''
        Obejtivo: Metodo que realiza o depósito na conta.
        Entrada: valor (float) e remetente (str).
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        op = 1
        # detecta se é uma transferencia
        if remetente != None:
            op = 2
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido")
            return False

    def sacar(self, valor, destinatario = None): 
        '''
        Obejtivo: Metodo que realiza o saque na conta.
        Entrada: valor (float) e destinatario (str).
        Return: True, se a operação foi realizada com sucesso. False, caso contrário a operação não foi realizada.
        '''
        op = 0
        #detecta se é uma transferencia e muda para op 2
        if destinatario != None:
            op = 2
        if valor <= self.saldo:
            self.saldo -= valor
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
    
    def transferir(self, valor, destinatario):
        '''
        Objetivo: Metodo que realiza uma transação.
        Entrada: valor (float) e obj contaBancaria
        Return: Se o ok -> True, Se o NOK -> False.
        '''
        # Se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular):
            # deposita na conta do destinatario
            destinatario.depositar(valor, self.titular)
        
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
    
    def adiciona_historico(self, tipo_transferencia, valor, tempo, saldo, destinatario = None):
        
        if tipo_transferencia == "Saque":
            if destinatario == None:
                self.historico.append({"tipo": f"{tipo_transferencia}",
                                        "remetente": self.titular,
                                        "destinatario": destinatario,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
            else:
                self.historico.append({"tipo": f"Transferência - {tipo_transferencia}",
                                        "remetente": self.titular,
                                        "destinatario": destinatario.titular,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
        elif tipo_transferencia == "Deposito":
            if destinatario == None:
                self.historico.append({"tipo": f"{tipo_transferencia}",
                                        "remetente": destinatario,
                                        "destinatario": self.titular,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
            else:
                self.historico.append({"tipo": f"Transferência - {tipo_transferencia}",
                                        "remetente": destinatario.titular,
                                        "destinatario": self.titular,
                                        "valor": valor,
                                        "tempo": tempo,
                                        "saldo": saldo})
        else:
            print(f"Transação {tipo_transferencia} invalida")