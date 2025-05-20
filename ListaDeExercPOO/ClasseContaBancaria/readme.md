## 2. Classe ContaBancaria
Crie a classe ContaBancaria .
### Na classe ContaBancaria , crie os seguintes atributos privados:
- **titular (String)**: Nome do titular da conta.
- **saldo (float)**: Saldo atual da conta.
- **limite (float)**: Limite de crédito da conta.
- **historico (list)**: Lista de transações realizadas.
### Na classe ContaBancaria , implemente os seguintes métodos:
- **depositar(valor: float)** : Adiciona um valor ao saldo da conta e registra a transação no histórico.
- **sacar(valor: float)** : Subtrai um valor do saldo da conta. Caso o saldo não
seja suficiente, permite o uso do limite de crédito. Registra a transação no
histórico.
- **transferir(valor: float, conta_destino)** : Transfere um valor para outra
conta bancária. Subtrai o valor do saldo da conta de origem e adiciona ao saldo
da conta de destino. Registra a transação no histórico de ambas as contas.

- **exibir_historico()** : Exibe todas as transações realizadas na conta.
- **exibir_saldo()** : Exibe o saldo atual da conta, incluindo o limite disponível.
### Crie uma classe TesteContaBancaria para instanciar objetos da classe ContaBancaria , definir seus atributos e testar os métodos.