## Tratamento de erros (try/except)
lista = [1,2,3]

while True:
    try:
        index = int(input("Digite o index da lista: "))
    except:
        print("Caracteres inválido")
        continue
    if index == -1:
        print("Saindo do loop")
        break
    try:
        print(lista[index])
    except:
        print("Index inválido")