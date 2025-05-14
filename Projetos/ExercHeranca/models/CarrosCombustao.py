from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    """Classe que representa um carro de combustão, herda Veiculos."""
    def __init__(self, placa: str, modelo: str, marca: str, 
                 ano: int, cor: str, valor_fipe: float, 
                 combustivel: str, nPortas: int, nAssentos: int, 
                 nCilindradas: int, nCambios: str) -> None:
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambios = nCambios
        
    def __str__(self) -> str:
        """Retorna uma string com as infos do carro de combustão"""
        # Adiciona o métofo __str__ da classe pai(Veiculos)
        infos = super().__str__()
        # Adiciona as infos especificas do carro de combustão
        infos += f"\nCombustível: {self.__combustivel}"
        infos += f"\nNúmero de Portas: {self.__nPortas}"
        infos += f"\nNúmero de Assentos: {self.__nAssentos}"
        infos += f"\nNúmero de Cilindradas: {self.__nCilindradas}"
        infos += f"\nNúmero de Câmbios: {self.__nCambios}"
        return infos