import os
from models.ProdutoAlimenticio import ProdutoAlimenticio
from models.ProdutoEletronico import ProdutoEletronico
from models.ConversorMoeda import ConversorMoeda
from models.excecao import MoedaInvalidaError

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto (em BRL): "))
    tipo = input("Digite o tipo do produto (alimenticio ou eletronico): ")

    if tipo.lower() == "alimenticio":
        validade = input("Digite a validade do produto (ex: 12/2025): ")
        produto = ProdutoAlimenticio(nome, preco, validade)
    
    elif tipo.lower() == "eletronico":
        garantia = input("Digite a garantia do produto (em meses): ")
        produto = ProdutoEletronico(nome, preco, garantia)
    
    else:
        print("Tipo de produto inválido!")
        return

    conversor = ConversorMoeda()

    try:
        if conversor.converte_preco_para_usd(produto):
            print("Conversão realizada com sucesso!")
        else:
            print("Conversão não necessária.")

    except MoedaInvalidaError as e:
        print(f"Erro de conversão: {e}")

    print("\nInformações do produto:")
    print(produto)

if __name__ == "__main__":
    main()