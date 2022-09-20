"""
    Crie uma função que recebe uma função como parâmetro
    e retorne o valor da função 2 executada.
"""


def soma(num1: int, num2: int) -> int:
    return num1 + num2


def exibir(func, *args):
    return func(*args)


print(exibir(soma, 10, 10))
