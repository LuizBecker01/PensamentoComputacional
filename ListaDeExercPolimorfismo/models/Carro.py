from .Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self._consumo = 12  # consumo específico do carro (km/L)

    def __str__(self) -> str:
        return super().__str__()
