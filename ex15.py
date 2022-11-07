# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    print(args)
    total = 1
    for n in args:
        try:
            n = float(n)
            total = total * n
        except ValueError:
            continue
    return total


numeros = []
while True:
    numeros.append(input('Digite o número: '))
    stop = input('Deseja continuar? [S/N]: ').upper()
    while stop not in ('S', 'N'):
        print('Digite apenas "S" ou "N"')
        stop = input('Deseja continuar? [S/N]: ').upper()
    if stop == 'N':
        break
print(multiplicar(*numeros))
