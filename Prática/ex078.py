# coding: utf-8

'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

print('Palpites MEGA SENA'.center(38, '-'))

quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

lista_de_jogos = []

for c in range(0, quantidade_jogos):
    jogo_temp = []

    while len(jogo_temp) < 6:
        numero_aleatorio = randint(1, 61)

        if numero_aleatorio not in jogo_temp:
            jogo_temp.append(numero_aleatorio)

    jogo_temp.sort()
    lista_de_jogos.append(jogo_temp)

for indice, jogo in enumerate(lista_de_jogos):
    sleep(1)

    print(f'Jogo {indice +1}: ', end='')

    for numero in jogo:
        print(f'{numero:^4}', end='|')

    print()
