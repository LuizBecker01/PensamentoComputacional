## Exercício: Sistema de Produtos e Conversão de Moedas

### Crie uma classe base chamada Produto com os seguintes requisitos:
 - Atributos privados: nome (str), preco (float) e moeda (str).
 - O construtor deve receber o nome e o preço em reais (BRL), e definir a moeda
    como "BRL".
 - Implemente métodos públicos para acessar e modificar cada atributo
    ( get_nome , set_nome , get_preco , set_preco , get_moeda , set_moeda ).
 - Implemente o método especial __str__ para exibir as informações do produto.
### Crie duas subclasses de Produto:
 - ProdutoAlimenticio e ProdutoEletronico , cada uma sobrescrevendo o
    método __str__ para mostrar informações específicas (polimorfismo).
### Crie uma classe chamada ConversorMoeda com:
 - Três atributos privados para as cotações:
    - 1 USD = 5.05 BRL
    - 1 EUR = 6.14 BRL
    - 1 EUR = 1.22 USD
 - Métodos para converter o preço do produto entre as moedas:
    - converte_preco_para_usd(produto: Produto) -> bool
    - converte_preco_para_eur(produto: Produto) -> bool
    - converte_preco_para_brl(produto: Produto) -> bool
 - Cada método deve alterar o preço e a moeda do produto conforme a conversão,
    retornando True se a conversão foi feita e False se não foi necessária.
 - Lance uma exceção personalizada ( MoedaInvalidaError ) se a moeda do
    produto não for reconhecida.
### No programa principal:
 - Peça ao usuário o nome, o preço e o tipo do produto ( alimenticio ou
    eletronico ).
 - Crie o objeto da subclasse correta usando herança e polimorfismo.
 - Tente converter o preço para dólar usando o método do conversor, tratando
    possíveis erros com try/except .
 - Mostre na tela o novo preço, a moeda e as informações do produto (usando
    polimorfismo com __str__ ).
##
**Dica:** Use encapsulamento para proteger os atributos e métodos das classes.