from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    """
    Classe que representa um carro eletrico, com as principais funcionalidades do sistema veiculos, com placas, veiculos, etc.
    """
    def __init__(self, placa: str, modelo: str, marca: str,
                 ano: int, cor: str, valor_fipe: float,
                 nAssentos: int, nPortas: int,
                 nivel_bateria: str, tipo_bateria: str,
                 autonomia: int) -> None:
        """Construtor da classe CarroEletrico"""
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
    
    def __str__(self) -> str:
        """Retorna uma string com as infos do carro eletrico"""
        # Adiciona o métofo __str__ da classe pai(Veiculos)
        infos = super().__str__()
        # Adiciona as infos especificas do carro eletrico
        infos += f"\nNúmero de Assentos: {self.__nAssentos}"
        infos += f"\nNúmero de Portas: {self.__nPortas}"
        infos += f"\nNivel de Bateria: {self.__nivel_bateria}"
        infos += f"\nTipo de Bateria: {self.__tipo_bateria}"
        infos += f"\nAutonomia: {self.__autonomia}"
        return infos