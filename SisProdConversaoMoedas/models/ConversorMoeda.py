"""Classe que representa um conversor de moedas."""
from models.excecao import MoedaInvalidaError

class ConversorMoeda:
    def __init__(self):
        self.__usd_brl = 5.05
        self.__eur_brl = 6.14
        self.__eur_usd = 1.22

    # Método para converter para USD
    def converte_preco_para_usd(self, produto):
        moeda_atual = produto.get_moeda()
        preco_atual = produto.get_preco()

        if moeda_atual == "USD":
            return False  # Se a modeda atual for EUR, retorna False

        elif moeda_atual == "BRL":
            novo_preco = preco_atual / self.__usd_brl
        elif moeda_atual == "EUR":
            novo_preco = preco_atual / self.__eur_usd
        else:
            raise MoedaInvalidaError(moeda_atual)

        produto.set_preco(novo_preco)
        produto.set_moeda("USD")
        return True

    # Método para converter para EUR
    def converte_preco_para_eur(self, produto):
        moeda_atual = produto.get_moeda()
        preco_atual = produto.get_preco()

        if moeda_atual == "EUR":
            return False  # Se a modeda atual for EUR, retorna False

        elif moeda_atual == "BRL":
            novo_preco = preco_atual / self.__eur_brl
        elif moeda_atual == "USD":
            novo_preco = preco_atual * self.__eur_usd
        else:
            raise MoedaInvalidaError(moeda_atual)

        produto.set_preco(novo_preco)
        produto.set_moeda("EUR")
        return True

    # Método para converter para BRL
    def converte_preco_para_brl(self, produto):
        moeda_atual = produto.get_moeda()
        preco_atual = produto.get_preco()

        if moeda_atual == "BRL":
            return False  # Se a modeda atual for EUR, retorna False

        elif moeda_atual == "USD":
            novo_preco = preco_atual * self.__usd_brl
        elif moeda_atual == "EUR":
            novo_preco = preco_atual * self.__eur_brl
        else:
            raise MoedaInvalidaError(moeda_atual)

        produto.set_preco(novo_preco)
        produto.set_moeda("BRL")
        return True