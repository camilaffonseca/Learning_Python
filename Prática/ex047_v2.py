# coding: utf-8

'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. (V.2)
'''

print('- Progressão Aritmética - \n')

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

print('Os 10 primeiros termos da progressão são...')

c = 1
while c <= 10:
    print(f'| {termo}', end = ' ')
    termo += razão 
    c += 1

print('| ...')
