import tkinter as tk
def clique():
    if rotulo.cget("text") == "Olá Mundo":
        rotulo.config(text="Você clicou no botão!")
    else:
        rotulo.config(text="Olá Mundo")

janela = tk.Tk()
janela.geometry("600x400")

rotulo = tk.Label(janela, text="Clique no botão abaixo:", font=("Arial", 16))
rotulo.pack(pady=10)

botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack(pady=10)

janela.mainloop()