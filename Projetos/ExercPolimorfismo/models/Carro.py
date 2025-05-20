from .Veiculos import Veiculos

class Carro(Veiculos):
    """
    Classe que representa um carro, herda da classe Veiculos.
    """
    
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        """Construtor da classe Carro"""
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        
    def __str__(self):
        return super().__str__()
        
    # Exercício 1: Polimorfismo com Consumo de Combustível
    def calcular_consumo(self, distancia: float) -> float:
        """Método que calcula o consumo de combustível do veículo.
        Argumento: distancia (float): distância percorrida em km
        Saída: consumo (float): litros de combustível consumidos
        """
        consumo = distancia / 12  # Supondo que o carro consome 12 km/l
        return consumo
