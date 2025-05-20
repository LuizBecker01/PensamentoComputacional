class livro:
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual

    def avancar_pagina(self): #Avança a leitura para a próxima página. A leitura não pode ultrapassar o número total de páginas.
        if self.pagina_atual < self.numero_paginas:
            self.pagina_atual += 1
        else:
            print("Nenhuma página para avançar")

    def voltar_pagina(self): #Volta a leitura para a página anterior. A leitura não pode ser menor que 1.
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
        else:
            print("Nenhuma página para voltar")

    def exibir_informacoes(self): #Exibe as informações do livro (título, autor, ano de publicação, número de páginas e páginas lidas).
        print(f"Título: {self.titulo} \nAutor: {self.autor} \nAno de Publicação: {self.ano_publicacao} \nNúmero de Páginas: {self.numero_paginas} \nPáginas Lidas: {self.pagina_atual}")