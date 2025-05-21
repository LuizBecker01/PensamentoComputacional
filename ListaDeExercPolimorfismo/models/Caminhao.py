from .Veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self._consumo = 5   # consumo especifico do caminhao (km/L)

    def __str__(self) -> str:
        return super().__str__()
    
    def calcular_consumo(self, distancia: float) -> float:
        return distancia / 5