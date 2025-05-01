class filme:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.avaliacao = avaliacao
    
    def exibir_informacoes(self): #Exibe as informações do filme (título, gênero, duração e avaliação).
        print(f"Título: {self.titulo} \nGênero: {self.genero} \nDuração: {self.duracao}m \nAvaliação: {self.avaliacao}")

    def avaliar(self, nova_avaliacao): #Altera a avaliação do filme para uma nova avaliação passada como parâmetro.
        self.avaliacao = nova_avaliacao

