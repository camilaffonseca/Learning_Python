# coding: utf-8

'''
Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador perder, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo.
'''


from random import randint
from unidecode import unidecode

print('Vamos jogar PAR OU ÍMPAR?')

vitórias_jogador = 0

while True:

    while True:
        jogador_opção = unidecode(input('\nPar ou ímpar? ').lower())
        if jogador_opção == 'par' or jogador_opção == 'impar':
            break
        else:
            print('Resposta inválida, digite PAR ou ÍMPAR...')

    while True:
        try:
            jogador_número = int(input('Valor: '))
            break
        except Exception:
            print('Resposta inválida, digite um número inteiro...')

    computador_número = randint(0, 10)

    número_final = jogador_número + computador_número

    if número_final % 2 == 0:
        número_final_verificado = 'par'
    else:
        número_final_verificado = 'impar'

    print(f'\nVocê jogou {jogador_número} e eu {computador_número}'
          f'\n{número_final} é {número_final_verificado}\n')

    if jogador_opção == número_final_verificado:
        vitórias_jogador += 1
        print('Você venceu ^^'
              '\nVamos jogar novamente...')
    else:
        print(f'Você perdeu com {vitórias_jogador} vitórias')
        break
