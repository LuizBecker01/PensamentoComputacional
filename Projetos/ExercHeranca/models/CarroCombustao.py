from .Veiculos import Veiculos

class CarroCombustao(Veiculos):
    """Classe que representa um carro de combustão, herda Veiculos."""
    def __init__(self, placa: str, modelo: str, marca: str, 
                 ano: int, cor: str, valor_fipe: float, 
                 combustivel: str, nPortas: int, nAssentos: int, 
                 nCilindrada: int, nCambio: str, nivel_combustivel: int) -> None:
        """Construtor da classe CarrosCombustao"""
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindrada
        self.__nCambios = nCambio
        self.__nivel_combustivel = nivel_combustivel
        
    def __str__(self) -> str:
        """Retorna uma string com as infos do carro de combustão"""
        # Adiciona o métofo __str__ da classe pai(Veiculos)
        infos = super().__str__()
        # Adiciona as infos especificas do carro de combustão
        infos += f"\nCombustível: {self.__combustivel}"
        infos += f"\nNúmero de Portas: {self.__nPortas}"
        infos += f"\nNúmero de Assentos: {self.__nAssentos}"
        infos += f"\nNúmero de Cilindrada: {self.__nCilindradas}"
        infos += f"\nCâmbio: {self.__nCambios}"
        infos += f"\nNível de Combustível: {self.__nivel_combustivel}"
        return infos
    
    def abastecer(self, percenual_adicionado: int) -> bool:
        """Método:
            Que abastece o carro de combustão.
        Argumentos:
            quantidade (int) - percentual adicionado ao nível de combustível.
        Retorna:
            True se o abastecimento for realizado com sucesso, False caso contrário.
        """
        novo_percenual = self.__nivel_combustivel + percenual_adicionado
        if novo_percenual <= 100: 
            self.__nivel_combustivel = novo_percenual
            return True
        else:
            print("Abastecimento não realizado, nível de combustível acima de 100%.")
            return False