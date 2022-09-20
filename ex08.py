"""
    Fizz Buzz - Se o parâmetro da função for divisível por 3,
    retorne Fizz. Se o parâmetro da função for divisível por 5,
    retorne Buzz. Se o parâmetro da função for divisível por 5 e 3,
    retorne FizzBuzz, caso contrário, retorne o número enviado.
"""


def fizz_buzz(num: int = 0) -> str | int:
    if num % 5 == 0 and num % 3 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num


print(fizz_buzz(int(input('Digite um número: '))))
