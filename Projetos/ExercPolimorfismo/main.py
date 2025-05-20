# Importando as classes necessárias
import os
from models.Veiculos import Veiculos
from models.Carro import Carro  
# from models.Moto import Moto
# from models.Caminhao import Caminhao


# Criando instâncias de cada classe
voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", 2018, "Vermelho", 47793)

# Criando um carro
uptsi = Veiculos("ABC1D00", "UP! TSI", "Volkswagen", 2021, "Branco", 66925)

# Criando uma moto
xl300 = Veiculos("BAC3E60", "XR 300L Tornado", "Honda", 2025, "Vermelho", 27690)

# Criando um caminhão
caminhao = Veiculos("CBA6D24", "Scania G 540", "Scania", 2022, "Prata", 702219)

# Exibindo as informações dos veículos
os.system('cls' if os.name == 'nt' else 'clear')
print("Informações dos veículos: ")
print("\n######## Veículo: #########")
print(voyage)
print("\n######## Carro: #########")
print(uptsi)
print("\n######## Moto: #########")
print(xl300)
print("\n######## Caminhão: #########")
print(caminhao)

