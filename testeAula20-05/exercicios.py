def div(a, b):
    if b == 0:
        return ValueError("Divisão por zero não é permitida.")
    return a / b

while True:
    try:
        n1 = input("Digite o primeiro número (ou somente 'SAIR' para sair): ")
        if n1.upper() == "SAIR":
            break
        n1 = float(n1)
        n2 = float(input("Digite o segundo número: "))
    except ValueError as e:
        print("Erro: Por favor, digite números válidos.")
        continue
    
resultado = div(n1, n2)
print(f"O resultado da divisão é: {resultado}")