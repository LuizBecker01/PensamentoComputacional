class veiculos: 
    def __init__(self, modelo, placa, marca, ano, cor, velocidade, latitude, longetude):
        self.modelo = modelo
        self.placa = placa
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longetude = longetude
        
    def acelerar(self):
        self.velocidade += 10
        nova_latitude = self.latitude + 1
        self.alterarLatitude(nova_latitude)
        
    def frenar(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            
    def mostrarInfos (self):
        print(f"O veiculo {self.modelo}, ano {self.ano}, de placa {self.placa}, está a {self.velocidade} km/h ")
        print(f"Lat: {self.latitude}, long: {self.longetude}")
        
    def alterarModelo (self, modelo):
        self.modelo = modelo
        
    def alterarPlaca (self, placa):
        self.placa = placa
    
    def alterarMarca (self, marca):
        self.marca = marca
        
    def alterarAno (self, ano):
        self.ano = ano
    
    def alterarCor (self, cor):
        self.cor = cor
    
    def alterarLatitude (self, latitude):
        self.latitude = latitude
    
    def alterarLongetude(self, longetude):
        self.longetude = longetude
        
    def obterPlaca(self):
        return self.placa