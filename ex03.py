def start():
    try:
        nome = str(input('Digite seu nome: '))
        if len(nome) <= 4:
            print("Seu nome é curto!")
        elif len(nome) <= 6:
            print('Seu nome é normal!')
        else:
            print('Seu nome é muito grande!')
    except ValueError:
        print('Seu nome não pode conter caracteres especiais ou números!')
        start()


start()
