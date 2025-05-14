from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico
import os

os.system('cls' if os.name == 'nt' else 'clear')

voyage = Veiculos("BCE9D36", "Voyage", "Wolkswagen",
                  2018, "Vermelho", 47793.00)

jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Volkswagen",
                            2025, "Vermelho", 250000.00, "Gasolina",
                            4, 5, 2000, "AT 7", 24)

tesla_model_s = CarroEletrico("JDN0A00", "Model S", "Tesla",
                        2021, "Branco", 950000.00, 4, 5, 65, "Lítio", 491)

fusca_eletrico = CarroConvEletrico("JDN0A01", "Fusca 1600 Eletrico", "Volkswagen",
                            1975, "Azul", 70000.00, "Gasolina",
                            4, 5, 2000, "MT 4", 24, 65, "Lítio", 150)

# print(voyage)
# print("--------------------------------------")
print(jetta_gli)
print("--------------------------------------")
# print(tesla_model_s)
if jetta_gli.abastecer(10):
    print("Abastecimento realizado com sucesso.")
else:
    print("Abastecimento não realizado.")
print("--------------------------------------")
print(jetta_gli)
print("--------------------------------------")
print(fusca_eletrico)