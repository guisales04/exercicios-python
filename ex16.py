# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
from os import system


def par_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Impar'


while True:
    system('cls')
    print('PAR OU IMPAR')
    try:
        n = int(input('Digite um numero: '))
    except ValueError:
        print('Digite um numero valido!')
        continue

    print(f'O numero {n} é {par_impar(n)}')

    stop = input('Deseja continuar? [S/N]: ').upper()

    while stop not in ('S', 'N'):
        print('Digite apenas "S" ou "N"')
        stop = input('Deseja continuar? [S/N]: ').upper()

    if stop == 'N':
        break
