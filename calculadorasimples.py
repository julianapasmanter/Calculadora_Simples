opcao = int(input("""Informe uma Opção: 
                  [1]Média Ponderada 
                  [2]Subtração 
                  [3]Multiplicação 
                  [4]Divisão 
                  [5]Potenciação """))

if opcao == 1:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    Mediap = (n1 + n2)/2

    print("A Média Ponderada é ",Mediap)

elif opcao == 2:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    if n1>n2:
        Subt = n1 - n2
        print("A subtração é ",Subt)
    elif n2>n1:
        Subt = n2 - n1
        print("A subtração é ",Subt)

if opcao == 3:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    Multp = n1 * n2

    print("A Multiplicação é ",Multp)

elif opcao == 4:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    Divs = n1 / n2

    if n2 != 0:
        print("A divisão é ",Divs)
    else:
        print("""Erro! 
              O Segundo valor deve ser diferente de Zero.""")
if opcao == 5:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    Poten = n1 ** n2

    print("A potenciação é ",Poten)

else:
    print("Opção invalida.")
    SystemExit




