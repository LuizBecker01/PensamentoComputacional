class Frota:
    def __init__(self):
        self._veiculos = []

    def adicionar_veiculo(self, veiculo):
        self._veiculos.append(veiculo)

    def mostrar_veiculos(self):
        for veiculo in self._veiculos:
            print(veiculo)

    def calcular_consumo_total(self, distancia):
        consumo_total = 0
        for veiculo in self._veiculos:
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total