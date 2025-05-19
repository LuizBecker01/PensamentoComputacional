from .CarroCombustao import CarroCombustao
from .CarroEletrico import CarroEletrico


class CarroConvEletrico(CarroCombustao, CarroEletrico):
    """Classe que implementea métodos específicos de um carro convertido
    em elétrico
    """

    def __init__(self,
                 placa: str,
                 modelo: str,
                 marca: str,
                 ano: int,
                 cor: str,
                 valor_fipe: float,
                 combustivel: str,
                 nPortas: int,
                 nAssentos: int,
                 nCilindrada: int,
                 nCambio: str,
                 nivel_combustivel: int,
                 nivel_bateria: int,
                 tipo_bateria: str,
                 autonomia: int) -> None:
        
        CarroCombustao.__init__(self,
                                placa=placa,
                                modelo=modelo,
                                marca=marca,
                                ano=ano,
                                cor=cor,
                                valor_fipe=valor_fipe,
                                combustivel=combustivel,
                                nPortas=nPortas,
                                nAssentos=nAssentos,
                                nCilindrada=nCilindrada,
                                nCambio=nCambio,
                                nivel_combustivel=nivel_combustivel)
        
        CarroEletrico.__init__(self,
                               placa=placa,
                               modelo=modelo,
                               marca=marca,
                               ano=ano,
                               cor=cor,
                               valor_fipe=valor_fipe,
                               nAssentos=nAssentos,
                               nPortas=nPortas,
                               nivel_bateria=nivel_bateria,
                               tipo_bateria=tipo_bateria,
                               autonomia=autonomia)

    def __str__(self) -> str:
        infos = CarroCombustao.__str__(self)
        infos += f"Nivel de bateria: {CarroEletrico.get_nivel_bateria(self)} "
        infos += f"Tipo de bateria: {CarroEletrico.get_tipo_bateria(self)} "
        infos += f"Autonomia: {CarroEletrico.get_autonomia(self)} "
        return infos

    def abastecer(self, percentual_adicionado: float) -> bool:
        """Método abastecer desativado
        Args:
            percentual_adicionado: float
        Returns:
            False, pois não pode abastcer
        """
        print("Carro convertida para elétrico! Não é mais possível abastecer!")
        return False
