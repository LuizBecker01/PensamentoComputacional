import re

class Veiculo:
    """
    Classe com as principais funcionalidades do sistema de veiculos, como placas, veiculos, etc.
    """
    def __init__( self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        """Construtor da classe Veiculo"""
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe
        self._consumo = 10  # valor padrão para ser sobrescrito nas subclasses

    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe:.2f}\n"
        return infos

    def calcular_consumo(self, distancia: float) -> float:
        return distancia / self._consumo