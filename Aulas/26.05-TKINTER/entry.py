import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    rotulo.config(text=f"Você digitou:{texto}")
    
janela = tk.Tk()
janela.title("Exemplo de Entry")
janela.geometry("300x150")
entrada = tk.Entry(janela, font=("Arial", 14))
entrada.pack(pady=10)
botao = tk.Button(janela, text="Mostrar Texto", command=mostrar_texto)
botao.pack(pady=10)
rotulo = tk.Label(janela, text="", font=("Arial", 14))
rotulo.pack(pady=10)
janela.mainloop()