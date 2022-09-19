"""
    Crie uma função que exibe uma saudação com os parametros saudacao e nome
"""


def saudacao(saudacao: str = 'Olá', nome: str = 'Usúario'):
    print(saudacao, nome)


saudacao('Boa Noite', input('Seu Nome: '))
