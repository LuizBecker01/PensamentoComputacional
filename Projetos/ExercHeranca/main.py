from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao
import os

os.system('cls' if os.name == 'nt' else 'clear')

voyage = Veiculos("BCE9D36", "Voyage", "Wolkswagen",
                  2018, "Vermelho", 47793.00)

jetta_gli = CarrosCombustao("JDM9D36", "Jetta GLI", "Volkswagen",
                            2025, "Vermelho", 250000.00, "Gasolina",
                            4, 5, 2000, "AT 7")

print(voyage)
print("--------------------------------------------------")
print(jetta_gli)
print("--------------------------------------------------")