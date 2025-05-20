import os
from models.Carro import Carro
from models.VeiculoEletrico import VeiculoEletrico
from models.Moto import Moto
from models.Caminhao import Caminhao
from models.Frota import Frota

# Limpa a tela
os.system('cls' if os.name == 'nt' else 'clear')

# Criação da frota
frota = Frota()

# Instanciando veículos
uptsi = Carro("ABC1C57", "UP! TSI", "Volkswagen", 2021, "Branco", 66925)
tornado = Moto("BBC2A09", "XR 300L Tornado", "Honda", 2025, "Vermelho", 27690)
R560 = Caminhao("CJC6B26", "R 560", "Scania", 2023, "Prata", 947858)
Dolphin = VeiculoEletrico("BYD8H89", "Dolphin Mini", "Build Your Dream", 2024, "Verde limão", 102851)

# Adicionando veículos à frota
frota.adicionar_veiculo(uptsi)
frota.adicionar_veiculo(tornado)
frota.adicionar_veiculo(R560)
frota.adicionar_veiculo(Dolphin)

# Exibindo todos os veículos da frota
print("== Veículos na frota ==")
frota.mostrar_veiculos()

# Distância a ser usada no cálculo
distancia = 240
print(f"\n== Consumo estimado para {distancia} km ==")

for veiculo in frota._veiculos:  # Acesso direto por simplicidade; em produção, prefira método getter
    consumo = veiculo.calcular_consumo(distancia)
    unidade = "kWh" if isinstance(veiculo, VeiculoEletrico) else "L"
    print(f"- {veiculo.get_placa()}: {consumo:.2f} {unidade}")

# Consumo total da frota
litros, kwh = frota.calcular_consumo_total(distancia)
print(f"\n== Consumo total da frota para {distancia} km ==")
print(f"- Combustível: {litros:.2f} litros")
print(f"- Elétrico: {kwh:.2f} kWh")

# Verificação de veículos duplicados (Exercício 5)
print("\n== Verificação de duplicidade ==")
duplicado = Carro("ABC1C57", "Outro Carro", "Outra Marca", 2022, "Azul", 50000)

if uptsi == duplicado:
    print(f"Veículo com placa {duplicado.placa} é considerado duplicado do UP TSI.")
else:
    print("Veículos diferentes.")

input("\nPressione enter para encerrar...")
