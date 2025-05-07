from models.contaBancaria import contaBancaria
import os

os.system('cls' if os.name=='nt' else 'clear') 

orlando = contaBancaria("Orlando", 1000, 500, []) # conta1
orlando.depositar(50)
henrique = contaBancaria("Henrique", 1000, 500, []) # conta2

henrique.transferir(50, orlando)
henrique.exibir_historico()
orlando.exibir_historico()