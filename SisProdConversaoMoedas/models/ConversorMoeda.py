"""Classe que representa um conversor de moedas."""
from models.excecao import MoedaInvalidaError

class ConversorMoeda:
    def __init__(self):
        # Tabela de taxas relativas
        self.taxas = {
            ('BRL', 'USD'): 1 / 5.05,
            ('USD', 'BRL'): 5.05,
            ('BRL', 'EUR'): 1 / 6.14,
            ('EUR', 'BRL'): 6.14,
            ('USD', 'EUR'): 1.22,
            ('EUR', 'USD'): 1 / 1.22
        }

    def converte(self, produto, moeda_destino):
        moeda_atual = produto.get_moeda()
        preco_atual = produto.get_preco()

        if moeda_atual == moeda_destino:
            return False  # Conversão desnecessária

        chave = (moeda_atual, moeda_destino)

        if chave not in self.taxas:
            raise MoedaInvalidaError(f"Conversão de {moeda_atual} para {moeda_destino} não suportada.")

        taxa = self.taxas[chave]
        novo_preco = preco_atual * taxa

        produto.set_preco(novo_preco)
        produto.set_moeda(moeda_destino)

        return True

    def converte_preco_para_usd(self, produto):
        return self.converte(produto, 'USD')

    def converte_preco_para_eur(self, produto):
        return self.converte(produto, 'EUR')

    def converte_preco_para_brl(self, produto):
        return self.converte(produto, 'BRL')