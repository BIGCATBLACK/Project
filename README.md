import tkinter as tk  # toolkit GUI padrão do Python

# Adiciona o texto do botão ao final do que já está no visor
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, atual + botao)

# Avalia a expressão do visor e mostra o resultado
def calcular():
    try:
        # ATENÇÃO: eval é prático, mas não é seguro para entradas não confiáveis
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Limpa o visor
def limpar():
    entrada.delete(0, tk.END)

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

# Visor
entrada = tk.Entry(
    janela, width=20, font=("Arial", 18),
    borderwidth=5, relief="ridge", justify="right"
)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Matriz de botões: (texto, linha, coluna)
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Cria os botões e posiciona na grade
for (texto, linha, coluna) in botoes:
    if texto == "=":
        tk.Button(
            janela, text=texto, width=5, height=2, font=("Arial", 14),
            command=calcular
        ).grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        tk.Button(
            janela, text=texto, width=5, height=2, font=("Arial", 14),
            command=lambda t=texto: clicar(t)
        ).grid(row=linha, column=coluna, padx=5, pady=5)

# Botão de limpar (C) ocupando 4 colunas
tk.Button(
    janela, text="C", width=22, height=2, font=("Arial", 14),
    command=limpar
).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Inicia o loop de eventos
janela.mainloop()
