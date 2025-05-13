from models.contaBancaria import contaBancaria
import os

menu = """
=========== MENU ===========
1 - Criar conta
2 - Exibir saldo
3 - Sacar
4 - Depositar
5 - Transferir
6 - Exibir histórico de transações
7 - Excluir conta
=============================
Digite a opção desejada: """

# Banco
Banco = [
    contaBancaria("João", 3300, 500, ["51980106042, "],[]),
    contaBancaria("Marco", 5000, 500, ["51980106041, "],[]),
    contaBancaria("Luiz", 6000, 700, ["51980106040, "],[])
]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    funcao = input(menu)

    if funcao == "1":
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo inicial: "))
        limite = float(input("Digite o limite da conta: "))
        Banco.append(contaBancaria(titular, saldo, limite, []))
        print("Conta criada com sucesso!")

    elif funcao == "2":
        titular = input("Titular da conta: ")
        for conta in Banco:
            if conta.titular == titular:
                print(f"Saldo atual de {titular}: R$ {conta.saldo:.2f}")
                break
        else:
            print("Conta não encontrada.")
            

    elif funcao == "3":
        titular = input("Titular da conta: ")
        valor = float(input("Valor do saque: "))
        for conta in Banco:
            if conta.titular == titular:
                conta.sacar(valor)
                break
        else:
            print("Conta não encontrada.")

    elif funcao == "4":
        titular = input("Titular da conta: ")
        valor = float(input("Valor do depósito: "))
        for conta in Banco:
            if conta.titular == titular:
                conta.depositar(valor)
                break
        else:
            print("Conta não encontrada.")

    elif funcao == "5":
        remetente_nome = input("Titular da conta que enviará: ")
        destinatario_nome = input("Titular da conta que receberá: ")
        valor = float(input("Valor da transferência: "))

        remetente = next((c for c in Banco if c.titular == remetente_nome), None)
        destinatario = next((c for c in Banco if c.titular == destinatario_nome), None)

        if remetente and destinatario:
            remetente.transferir(valor, destinatario)
        else:
            print("Conta(s) não encontrada(s).")

    elif funcao == "6":
        titular = input("Titular da conta: ")
        for conta in Banco:
            if conta.titular == titular:
                conta.exibir_historico()
                break
        else:
            print("Conta não encontrada.")

    elif funcao == "7":
        titular = input("Titular da conta a ser excluída: ")
        for conta in Banco:
            if conta.titular == titular:
                if conta.saldo == 0:
                    Banco.remove(conta)
                    print("Conta excluída com sucesso.")
                else:
                    print("A conta não pode ser excluída. Saldo precisa estar zerado.")
                break
        else:
            print("Conta não encontrada.")

    else:
        print("Opção inválida.")

    input("\nPressione ENTER para continuar...")
