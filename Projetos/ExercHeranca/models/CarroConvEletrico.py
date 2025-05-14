from .CarroCombustao import CarroCombustao

class CarroConvEletrico(CarroCombustao):
    """Classe que representa um carro de combustão convertido para elétrico, herda CarroCombustao."""
    def __init__(self, placa: str, modelo: str, marca: str, 
                 ano: int, cor: str, valor_fipe: float, 
                 combustivel: str, nPortas: int, nAssentos: int, 
                 nCilindrada: int, nCambio: str, nivel_combustivel: int, 
                 nivel_bateria: str, tipo_bateria: str, autonomia: int) -> None:
        """Construtor da classe CarroConvEletrico"""
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe, combustivel, 
                         nPortas, nAssentos,nCilindrada, nCambio, nivel_combustivel)
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
        
        