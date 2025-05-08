from models.contaBancaria import contaBancaria
import os
import time

menu = "Selecione a operação desejada!"
menu += "\n1 - Criar conta;"
menu += "\n2 - Exibir saldo;"
menu += "\n3 - Sacar;"
menu += "\n4 - Depositar;"
menu += "\n5 - Realizar transferência;"
menu += "\n6 - Exibir histórico de transações;"
menu += "\n7 - Excluir conta."
menu += "\n"

os.system('cls' if os.name=='nt' else 'clear') 

while True:
    funcao = input(menu)
    
    time.sleep(2)
    
    Banco = []

    Banco.append(contaBancaria("João", 1300, 500, []))
    Banco.append(contaBancaria("Marco", 5000, 500, []))
    Banco.append(contaBancaria("Pedro", 2000, 700, []))

    titular = input("Digite o titular da conta que deseja ver o saldo:")
    for conta in Banco:
        if conta.titular == titular:
            print(f"O {titular} tem R$ {conta.saldo} em sua conta.")
        # else:
        #     if conta.tituar != titular:
        #         print(f"O titular não foi encntrado.")
    break  