# Importando as classes necessárias
import os
from ListaDeExercPolimorfismo.models.Veiculo import Veiculo
from models.Carro import Carro

# Criando instâncias de cada classe
voyage = Veiculo("BCE9D36", "Voyage", "Volkswagen", 2018, "Vermelho", 47793)

# Criando um carro
uptsi = Carro("ABC1C00", "UP! TSI", "Volkswagen", 2021, "Branco", 66925)

# Exibindo as informações dos veículos
os.system('cls' if os.name == 'nt' else 'clear')
print("Informações dos veículos: ")
print("\n### Veículo: ###")
print(voyage)
print("\n### Carro: ###")
print(uptsi)

