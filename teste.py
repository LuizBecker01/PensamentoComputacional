import time

#   Mensagem com opções
op_string = "Digite:"
op_string += "\nad para adicionar filme;"
op_string += "\nrm para remover filme;"
op_string += "\ned para editar filme;"
op_string += "\nls para listar todos os filmes;"
op_string += "\nou (sair) para encerrar!"
op_string += "\n"

#   Lista para armazenar os filmes
filmes = []

#   Função que calcula a média das notas
def media(filmes):
    if len(filmes) == 0:
        return 0
    soma = 0
    for filme in filmes:
        soma += filme["nota"]
    return round(soma / len(filmes), 2)

#   Função que verifica duplicidade
def duplicidade(nome, filmes):
    for filme in filmes:
        if nome.lower() == filme["nome"].lower():
            return True
    return False

#   Função que imprime todos os filmes
def imprime_filmes(filmes):
    if not filmes:
        print("Nenhum filme cadastrado ainda.")
        return
    for filme in filmes:
        print(f"O filme '{filme['nome']}' recebeu a nota {filme['nota']} da crítica!")

#   Início do programa
while True:
    print(op_string)
    operacao = input("Escolha a operação: ").strip().lower()

    #   Adicionar filme
    if operacao == 'ad':
        nome = input("Digite o nome do filme: ").strip()
        if duplicidade(nome, filmes):
            print(f"O filme '{nome}' já está cadastrado!")
            continue
        try:
            nota = float(input("Digite a nota do filme (0.0 a 10.0): "))
            if 0.0 <= nota <= 10.0:
                filmes.append({"nome": nome, "nota": nota})
                print(f"Filme '{nome}' adicionado com sucesso!")
                time.sleep(1)
            else:
                print("A nota deve estar entre 0.0 e 10.0.")
                time.sleep(1)
        except ValueError:
            print("Nota inválida. Digite um número.")
        imprime_filmes(filmes)

    #   Remover filme
    elif operacao == 'rm':
        nome = input("Digite o nome do filme que deseja remover: ").strip()
        removido = False
        for filme in filmes:
            if filme["nome"].lower() == nome.lower():
                filmes.remove(filme)
                print(f"Filme '{nome}' removido com sucesso.")
                removido = True
                break
        if not removido:
            print(f"Filme '{nome}' não encontrado.")

    #   Editar nota de filme
    elif operacao == 'ed':
        nome = input("Digite o nome do filme que deseja editar: ").strip()
        for filme in filmes:
            if filme["nome"].lower() == nome.lower():
                try:
                    nova_nota = float(input(f"Digite a nova nota para '{nome}': "))
                    if 0.0 <= nova_nota <= 10.0:
                        filme["nota"] = nova_nota
                        print(f"Nota do filme '{nome}' atualizada com sucesso!")
                    else:
                        print("A nota deve estar entre 0.0 e 10.0.")
                except ValueError:
                    print("Nota inválida.")
                break
        else:
            print(f"Filme '{nome}' não encontrado.")

    #   Listar todos os filmes
    elif operacao == 'ls':
        time.sleep(1)
        imprime_filmes(filmes)

    #   Sair do programa
    elif operacao == 'sair':
        print("\n🎬 Encerrando o sistema.")
        time.sleep(1.5)
        imprime_filmes(filmes)
        time.sleep(1)
        print(f"\n🎯 Média das notas: {media(filmes)}")
        break

    else:
        print("Operação inválida. Tente novamente.")