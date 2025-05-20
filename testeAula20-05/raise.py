class MinhaExcecao(Exception):
    pass

def dividir(a, b):
    if b == 0:
        raise MinhaExcecao("Divisão por zero não é permitida.")
    return a / b
try:
    print(dividir(10, 0))
except MinhaExcecao as erro:
    print(f"Erro personalizado: {erro}")