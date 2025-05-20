# Importando as classes necessárias
import os
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao

# Criando instâncias de cada classe
uptsi = Carro("ABC1C57", "UP! TSI", "Volkswagen", 2021, "Branco", 66925)
tornado = Moto("BBC2A09", "XR 300L Tornado", "Honda", 2025, "Vermelho", 27690)
R560 = Caminhao("CJC6B26", "R 560", "Scania", 2023, "Prata", 947858)

# Exibindo as informações dos veículos
os.system('cls' if os.name == 'nt' else 'clear')
print("Informações dos veículos: ")
print("\n===Carro===")
print(uptsi)
print("\n===Moto===")
print(tornado)
print("\n===Caminhão===")
print(R560)


# Calculando consumo
distancia = 240
print(f"Consumo UP TSI, estimado para {distancia} km: {uptsi.calcular_consumo(distancia):.2f} L")
print(f"Consumo da Tornado, estimado para {distancia} km: {tornado.calcular_consumo(distancia):.2f} L")
print(f"Consumo do R 560, estimado para {distancia} km: {R560.calcular_consumo(distancia):.2f} L")

input("\nPressione enter para encerrar...")
