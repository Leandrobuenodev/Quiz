while True:

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    operacao = input("Digite a operação (+, -, /, *): ")
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro divisão por 0"
    else:
        resultado = "operação invalida"

    print("resultado: ", resultado)

    sair = input("Quer continuar? (s/n): ").lower()
    if sair == "n":
        print("Encerrando a calculadora.. Até mais!")
        break
