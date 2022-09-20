"""
    Crie uma função que recebe uma função como parâmetro
    e retorne o valor da função 2 executada.
    Faça a função 1 executar duas funções que recebam
    um número diferente de argumentos.
"""


def soma(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


def multi(num1: int, num3: int) -> int:
    return num1 * num3


def exibir(func, *args, **kwargs):
    return func(*args, **kwargs)


print(exibir(soma, 10, 10, 30))
print(exibir(multi, 10, 30))
