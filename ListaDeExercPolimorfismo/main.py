# Importando as classes necessárias
import os
from models.Carro import Carro

# Criando instâncias de cada classe
uptsi = Carro("ABC1C00", "UP! TSI", "Volkswagen", 2021, "Branco", 66925)

# Exibindo as informações dos veículos
os.system('cls' if os.name == 'nt' else 'clear')
print("Informações dos veículos: ")
print("\n### Carro: ###")
print(uptsi)  

# Calculando consumo
distancia = 240
print(f"\nConsumo estimado para {distancia} km: {uptsi.calcular_consumo(distancia):.2f} L")

input("\nPressione enter para encerrar...")
