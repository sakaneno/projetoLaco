


n = 2

while n != 1:
    print("+++++++++++++++++MENU++++++++++++++")
    print(("1) - Soma"))
    print(("2) - Subtração"))
    print(("3) - Multiplicação"))
    print(("4) - Subtração"))
    print(("0) - Sair do Programa!"))
    opcao = int(input("Digite uma opção:: "))

    if opcao == 1:
        val1 = int(input("Digite o valor: "))
        val2 = int(input("Digite outro valor:"))
        print(f"A Soma é: {val1 + val2}")
        n = 2
    elif opcao == 2:
        val1 = int(input("Digite o valor: "))
        val2 = int(input("Digite outro valor:"))
        print(f"A Subtração é: {val1 - val2}")
        n = 2
    elif opcao == 3:
        val1 = int(input("Digite o valor: "))
        val2 = int(input("Digite outro valor:"))
        print(f"A Multiplicação é: {val1 * val2}")
        n = 2
    elif opcao == 4:
        val1 = int(input("Digite o valor: "))
        val2 = int(input("Digite outro valor:"))
        print(f"A Divisão é: {val1 / val2}")
        n = 2
    elif opcao == 0:
        print("Saindo já!!!!!")
        n = 1
    else:
        print("Operador inválido!")
        n = 2