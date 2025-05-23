"""Classe base para representar um produto."""
class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__moeda = "BRL"

    # Métodos getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_moeda(self):
        return self.__moeda
    
    # Métodos setters
    def set_nome(self, nome: str):
        self.__nome = nome

    def set_preco(self, preco: float):
        self.__preco = preco

    def set_moeda(self, moeda: str):
        self.__moeda = moeda

    # Método especial __str__
    def __str__(self):
        return f"Produto: {self.__nome}\nPreco: {self.__preco:.2f}\nMoeda: {self.__moeda}"