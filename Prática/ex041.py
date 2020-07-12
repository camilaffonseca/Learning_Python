# coding: utf-8

# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

itens = ['PEDRA', 'PAPEL', 'TESOURA']

jogador = int(input('Sua vez:'
                    '\n[0] Pedra'
                    '\n[1] Papel'
                    '\n[2] Tesoura'
                    '\n>>> '
                    ))

computador = randint(0, 2)

x = ['JO', 'KEN', 'PÔ!', '...']

for item_x in x:
    print(item_x)
    sleep(1)

print(f'Eu joguei {itens[computador]}'
      f'\nVocê jogou {itens[jogador]}')

if computador == jogador:
    print('> Empate <')
elif jogador == computador -1:
    print('Eu venci :)')
elif computador == jogador -1:
    print('Você venceu ^^')
