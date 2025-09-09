def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


while True:
    print("\n===== CALCULADORA =====")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando...")
        break

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", soma(n1, n2))
    elif opcao == "2":
        print("Resultado:", subtracao(n1, n2))
    elif opcao == "3":
        print("Resultado:", multiplicacao(n1, n2))
    elif opcao == "4":
        print("Resultado:", divisao(n1, n2))
    else:
        print("Opção inválida, tente novamente.")
