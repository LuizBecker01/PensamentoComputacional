class DistanciaNegativa(Exception):
    """Exceção para distância negativa."""
    pass

distancia = float(input("Digite a distância: "))
try:
    if distancia < 0:
        raise DistanciaNegativa("A distância deve ser maior que zero.")
except ValueError as erro:
    print(f"Erro: {erro}. Por favor, digite um número válido.")
except DistanciaNegativa as erro:
    print(f"Erro: {erro}.")


