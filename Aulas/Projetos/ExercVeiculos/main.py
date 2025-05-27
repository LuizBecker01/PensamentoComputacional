from models.veiculos import veiculos
gol = veiculos("Gol Copa",  "IND-1010", "Volkswagen", 
               2006, "Amarelo", 0, 0, 0)

gol.mostrarInfos()
gol.acelerar()
gol.mostrarInfos()
gol.frenar()
gol.mostrarInfos()