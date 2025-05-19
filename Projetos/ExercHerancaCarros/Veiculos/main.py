# Importando as classes necessárias
from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico

# Criando instâncias de cada classe
voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", 2018, "Vermelho", 47793)

# Criando um carro a combustão
jetta_gli = CarroCombustao(placa="JDM9D36",
                           modelo="Jetta GLI",
                           marca="Volkswagen",
                           ano=2025,
                           cor="Vermelho",
                           valor_fipe=250000,
                           combustivel="Gasolina",
                           nPortas=4,
                           nAssentos=5,
                           nCilindrada=2000,
                           nCambio="AT 7",
                           nivel_combustivel=24)

# Criando um carro elétrico
tesla_model_s = CarroEletrico(placa="JDN0A00",
                              modelo="Tesla Model S",
                              marca="Tesla",
                              ano=2021,
                              cor="Branco",
                              valor_fipe=950000,
                              nAssentos=5,
                              nPortas=4,
                              nivel_bateria=65,
                              tipo_bateria="Lítio",
                              autonomia=491)

# Criando um carro convertido em elétrico (combustão + elétrico)
# (herança múltipla)
fusca_eletrico = CarroConvEletrico(placa="IAA0D36",
                                   modelo="Fusca 1600 Elétrico",
                                   marca="Volkswagen",
                                   ano=1975,
                                   cor="Azul",
                                   valor_fipe=70000,
                                   combustivel="Gasolina",
                                   nPortas=4,
                                   nAssentos=5,
                                   nCilindrada=1600,
                                   nCambio="MT 4",
                                   nivel_combustivel=24,
                                   tipo_bateria="Lítio",
                                   autonomia=150,
                                   nivel_bateria=65)

# Exibindo as informações dos veículos
print("Informações dos veículos: ")
print("\n\n######## Veículo: #########")
print(voyage)
print("\n\n######## Carro a combustão: #########")
print(jetta_gli)
print("\n\n######## Carro elétrico: #########")
print(tesla_model_s)
print("\n\n######## Carro convertido em elétrico: #########")
print(fusca_eletrico)
# Abastecendo o carro a combustão
jetta_gli.abastecer(10)
print(jetta_gli)
# Abastecendo o carro convertido em elétrico
fusca_eletrico.abastecer(10)
# Exibindo as informações do carro convertido em elétrico
print("\n\n######## Carro conv. elétrico após abastecimento: #########")
print(fusca_eletrico)
