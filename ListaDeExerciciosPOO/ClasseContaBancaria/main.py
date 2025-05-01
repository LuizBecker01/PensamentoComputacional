# from models.contaBancaria import contaBancaria

# conta1 = contaBancaria("Orlando", 900, 800, ["Deposito de 150 reais"])
# conta2 = contaBancaria("Ian", 3000, 1000, ["Deposito de 900 reais"])

# conta1.depositar(150)
# conta1.sacar(90)
# conta1.transferir(100, conta2)
# # conta1.exibir_historico()
# # conta1.exibir_saldo()

# conta2.depositar(900)
# conta2.sacar(570)
# conta2.transferir(140, conta1)
# # conta2.exibir_historico()
# # conta2.exibir_saldo()

# print("\n>>> Histórico do Orlando:")    
# conta1.exibir_historico()
# print("\n>>> Histórico do Ian:")
# conta2.exibir_historico()

# print("\n>>> Saldo do Orlando:")
# conta1.exibir_saldo()
# print("\n>>> Saldo do Ian:")
# conta2.exibir_saldo()


from teste_contaBancaria import TesteContaBancaria

teste = TesteContaBancaria()
teste.executar_testes()