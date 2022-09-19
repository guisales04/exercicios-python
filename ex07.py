"""
    Crie uma função que receba 2 números.
    O primeiro é um valor e o segundo um percentual (ex. 10%).
    Retorne o valor do primeiro número
    somado do aumento do percentual do mesmo.
"""


def soma(valor: int | float = 0, percentual: int | float = 0) -> int | float:
    total = valor + (valor * percentual / 100)
    return total


print(soma(250, 10))
