from models.contaBancaria import contaBancaria
import os

os.system('cls' if os.name=='nt' else 'clear') 

conta = contaBancaria("Orlando", 1000, 500, [])

conta.depositar(150)
conta.sacar(100)
conta.exibir_historico()