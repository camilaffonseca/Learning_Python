# coding: utf-8

'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print('- Progressão Aritmética - \n')

termo1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

print('Os 10 primeiros termos da progressão são...')

for c in range(0, 10):
    print(f'{termo1} | ', end='')
    termo1 += razão

print('...')
