# coding: utf-8

'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''


from random import randint


def perguntar_numero(mensagem) -> int:
    '''Doc string'''

    return int(input(mensagem))


numero = randint(0, 10)
cont = 1

numero_usuario = perguntar_numero(
    'Adivinhe em que número eu estou pensando :) \n> '
)


while numero != numero_usuario:
    if numero > numero_usuario:
        numero_usuario = perguntar_numero('Mais... Tente novamente (: \n> ')
    elif numero < numero_usuario:
        numero_usuario = perguntar_numero('Menos... Tente novamente (: \n> ')
    cont += 1

print(f'Vc acertou com {cont} tentativas ^^')
