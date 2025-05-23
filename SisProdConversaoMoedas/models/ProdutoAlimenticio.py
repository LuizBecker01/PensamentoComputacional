"""Subclasse da classe Produto, responsável por representar um produto alimenticio."""
from models.Produto import Produto


class ProdutoAlimenticio(Produto):
    def __init__(self, nome: str, preco: float, validade: str) -> None:
        super().__init__(nome, preco)
        self.__validade = validade

    def get_validade(self):
        return self.__validade
    
    def set_validade(self, validade: str):
        self.__validade = validade

    def __str__(self):
        return f"Alimento: {self.get_nome()}\nPreco: {self.get_preco():.2f}\nMoeda: {self.get_moeda()}\nValidade: {self.__validade}"