from models.VeiculoEletrico import VeiculoEletrico

class Frota:
    def __init__(self):
        self._veiculos = []

    def adicionar_veiculo(self, veiculo):
        self._veiculos.append(veiculo)

    def mostrar_veiculos(self):
        print("\nVeículos na frota:")
        for veiculo in self._veiculos:
            print(f"- {veiculo._Veiculo__modelo}")

    def calcular_consumo_total(self, distancia: float) -> float:
        total_litros = 0  # Inicializando o consumo em litros
        total_kwh = 0  # Inicializando o consumo em kWh

        for veiculo in self._veiculos:
            consumo = veiculo.calcular_consumo(distancia)
            if isinstance(veiculo, VeiculoEletrico):
                total_kwh += consumo
            else:
                total_litros += consumo

        return total_litros, total_kwh