# coding: utf-8

'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário em Python. No final,
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
'''

from random import randint
from operator import itemgetter
from time import sleep

jogadas = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('\nValores sorteados:\n')

for k, v in jogadas.items():
    print(f'{k}: {v}')
    sleep(0.5)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('\n - Ranking - \n')

for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
