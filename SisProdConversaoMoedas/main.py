import os
from models.Produto import Produto
from models.ProdutoAlimenticio import ProdutoAlimenticio
from models.ProdutoEletronico import ProdutoEletronico

os.system('cls' if os.name == 'nt' else 'clear')

p = Produto("Notebook", 3000.00)
pa = ProdutoAlimenticio("Arroz", 5.00, "2023-12-31")
pe = ProdutoEletronico("Smartphone", 2000.00, "12")

print(p)
print(pa)
print(pe)