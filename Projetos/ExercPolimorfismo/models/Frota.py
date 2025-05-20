class Frota:
    def __init__(self):
        self.__lista = []

    def adicionar_veiculo(self, veiculo):
        self.__lista.append(veiculo)

    def __str__(self):
        """Retorna uma string com as informações da frota"""
        infos = ""
        for veiculo in self.__lista:
            infos += str(veiculo) + "\n"
        return infos