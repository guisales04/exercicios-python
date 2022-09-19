while True:
    try:
        n = int(input("Digite um número: "))

        if n % 2 == 0:
            print("O número digitado é par")

        else:
            print("O número digitado é impar")

        continuar = str(input("Deseja continuar? [S/N] ")).upper()

        while continuar not in "S/N":
            continuar = str(input("Deseja continuar? [S/N] ")).upper()

        if continuar == 'N':
            break

    except ValueError:
        print("Por favor insira um número inteiro válido!")
