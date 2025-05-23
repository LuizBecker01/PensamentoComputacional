"""Subclasse da classe Produto, responsável por representar um produto alimenticio."""
from models.Produto import Produto

class ProdutoEletronico(Produto):
    def __init__(self, nome: str, preco: float, garantia: int) -> None:
        super().__init__(nome, preco)
        self.__garantia = garantia

    def get_garantia(self):
        return self.__garantia
    
    def set_garantia(self, garantia: int):
        self.__garantia = garantia

    def __str__(self):
        return f"Eletronico: {self.get_nome()}\nPreco: {self.get_preco():.2f}\nMoeda: {self.get_moeda()}\nGarantia: {self.__garantia} meses"