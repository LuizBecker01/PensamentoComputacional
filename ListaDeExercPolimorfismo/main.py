# Importando as classes necessárias
import os
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao
from models.Frota import Frota

os.system('cls' if os.name == 'nt' else 'clear')

frota = Frota()

# Criando instâncias de cada classe
uptsi = Carro("ABC1C57", "UP! TSI", "Volkswagen", 2021, "Branco", 66925)
tornado = Moto("BBC2A09", "XR 300L Tornado", "Honda", 2025, "Vermelho", 27690)
R560 = Caminhao("CJC6B26", "R 560", "Scania", 2023, "Prata", 947858)

# Exibindo as informações dos veículos
# print("Informações dos veículos: ")
# print("===Carro===")
# print(uptsi)
# print("===Moto===")
# print(tornado)
# print("===Caminhão===")
# print(R560)

# Adicionando os veículos na frota
frota.adicionar_veiculo(uptsi)
frota.adicionar_veiculo(tornado)
frota.adicionar_veiculo(R560)

# Exibindo os veículos da frota
frota.mostrar_veiculos()

# Calculando consumo por veiculo
distancia = 240
print(f"Consumo UP TSI, estimado para {distancia} km: {uptsi.calcular_consumo(distancia):.2f} L")
print(f"Consumo da Tornado, estimado para {distancia} km: {tornado.calcular_consumo(distancia):.2f} L")
print(f"Consumo do R 560, estimado para {distancia} km: {R560.calcular_consumo(distancia):.2f} L")

# Calculando consumo total da frota
print(f"\nConsumo total da frota estimado para {distancia} km: {frota.calcular_consumo_total(distancia):.2f} litros")

input("\nPressione enter para encerrar...")
