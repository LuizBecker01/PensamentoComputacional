import os
from models.ProdutoAlimenticio import ProdutoAlimenticio
from models.ProdutoEletronico import ProdutoEletronico
from models.ConversorMoeda import ConversorMoeda
from models.excecao import MoedaInvalidaError

os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_produto(produtos, conversor):
    nome = input("Digite o nome do produto: ")

    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            break
        except ValueError:
            print("Preço inválido. Digite um número válido.")

    # Validação da moeda de origem
    while True:
        moeda_origem = input("Digite a moeda atual do produto (BRL, USD, EUR): ").upper()
        if moeda_origem in ["BRL", "USD", "EUR"]:
            break
        else:
            print("Moeda inválida. Escolha entre BRL, USD ou EUR.")

    # Validação do tipo de produto
    while True:
        tipo = input("Digite o tipo do produto (alimenticio ou eletronico): ").lower()
        if tipo == "alimenticio":
            validade = input("Digite a validade do produto (ex: 12/2025): ")
            produto = ProdutoAlimenticio(nome, preco, validade)
            break
        elif tipo == "eletronico":
            garantia = input("Digite a garantia do produto (em meses): ")
            produto = ProdutoEletronico(nome, preco, garantia)
            break
        else:
            print("Tipo de produto inválido. Digite 'alimenticio' ou 'eletronico'.")

    produto.set_moeda(moeda_origem)

    # Validação da moeda de destino
    while True:
        moeda_destino = input("Digite a moeda para a qual deseja converter o preço (BRL, USD, EUR): ").upper()
        if moeda_destino in ["BRL", "USD", "EUR"]:
            break
        else:
            print("Moeda inválida. Escolha entre BRL, USD ou EUR.")

    try:
        if conversor.converte(produto, moeda_destino):
            print("Conversão realizada com sucesso!")
        else:
            print("Conversão não necessária.")
    except MoedaInvalidaError as e:
        print(f"Erro de conversão: {e}")

    print("\nInformações do produto:")
    print(produto)

    # Adiciona o produto à lista
    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")

def ver_produtos(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado ainda.\n")
    else:
        print("\nProdutos cadastrados:")
        for i, p in enumerate(produtos, start=1):
            print(f"{i} - {p}")
        print()

def main():
    produtos = []
    conversor = ConversorMoeda()

    while True:
        print("=== Menu ===")
        print("1 - Cadastrar Produto")
        print("2 - Ver Produtos Cadastrados")
        print("3 - Sair")

        opcao = input(f"\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos, conversor)
        elif opcao == "2":
            ver_produtos(produtos)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()