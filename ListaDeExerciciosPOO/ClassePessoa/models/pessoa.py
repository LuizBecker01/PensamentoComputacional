class pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e {self.altura:.2f} de altura.")

    def aniversario(self): #Aumenta a idade da pessoa em 1.
        self.idade += 1

    def crescer(self, valor=0.05): #Aumenta a altura da pessoa em um valor passado como parâmetro.
        self.altura += valor
    
    def exibir_informacoes(self): #Exibe as informações da pessoa (nome, idade e altura).
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e {self.altura:.2f} de altura.")