class Veiculos:
    """
    Classe com as principais funcionalidades do sitema veiculos, com placas, veiculos, etc.
    """
    def __init__(self, placa: str, modelo: str, marca: str, 
                 ano: int, cor: str, valor_fipe: float) -> None:
        """"Consultor da classe Veiculos"""
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe
    
    def __str__(self) -> str:
        """Retorna uma string com as infos do veicolo"""
        infos = f"Placa: {self.__placa}"
        infos += f"\nModelo: {self.__modelo}"
        infos += f"\nMarca: {self.__marca}"
        infos += f"\nAno: {self.__ano}"
        infos += f"\nCor: {self.__cor}"
        infos += f"\nValor Fipe: {self.__valor_fipe}"
        return infos
    
    def getPlaca(self):
        """Retorna a placa do veiculo"""
        return self.__placa
    
    # def getModelo(self):
    #     """Retorna o modelo do veiculo"""
    #     return self.__modelo
    
    # def getMarca(self):
    #     """Retorna a marca do veiculo"""
    #     return self.__marca
    
    # def getAno(self):
    #     """Retorna o ano do veiculo"""
    #     return self.__ano
    
    # def getCor(self):
    #     """Retorna a cor do veiculo"""
    #     return self.__cor
    
    # def getValor_fipe(self):
    #     """Retorna o valor fipe do veiculo"""
    #     return self.__valor_fipe