import tkinter as tk
def mostrar_opcao():
    texto = f"Escolheu: {opcao1.get()}"
    texto += f" {opcao2.get()}"
    texto += f" {opcao3.get()}"
    rotulo.config(text= texto)
    
    if opcao1.get():
        if opcao2.get():
            if opcao3.get():
               
    
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("600x500")
opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()
opcao = tk.StringVar(value="A")
tk.Radiobutton(janela, text="Dinheiro", font=("Arial", 12), variable=opcao1, 
               value=True, command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Tempo", font=("Arial", 12), variable=opcao2, 
               value=True, command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Saúde", font=("Arial", 12), variable=opcao3, 
               value=True, command=mostrar_opcao).pack()
rotulo = tk.Label(janela, text="Escolheu: ", font=("Arial", 12))
rotulo.pack(pady=10)
tk.Button(janela, text="Sair", font=("Arial", 12), command=janela.destroy).pack(pady=10)
janela.mainloop()