from .Veiculo import Veiculo

class VeiculoEletrico(Veiculo):
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
    
    def __str__(self) -> str:
        return super().__str__()
    
    def calcular_consumo(self, distancia: float) -> float:
        return distancia * 0.15    # consumo específico do carro eletrico (kWh/km)

    def recarregar(self):
        print(f"{self.Veiculo__modelo} está sendo carregado.")