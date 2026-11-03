# Calculadora simples em Python

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero."
    return a / b


def main():
    while True:
        print("\n===== CALCULADORA =====")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: digite apenas números.")
            continue

        if opcao == "1":
            resultado = somar(num1, num2)
        elif opcao == "2":
            resultado = subtrair(num1, num2)
        elif opcao == "3":
            resultado = multiplicar(num1, num2)
        else:
            resultado = dividir(num1, num2)

        print("Resultado:", resultado)


main()
