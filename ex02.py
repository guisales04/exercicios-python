def start():
    try:
        hora = int(input("Digite a hora: "))

        if hora >= 0 and hora <= 11:
            print("Bom Dia!")
        elif hora <= 17:
            print("Boa Tarde!")
        elif hora <= 23:
            print("Boa Noite!")
    except ValueError:
        print("Insira um horario valido!")


start()
