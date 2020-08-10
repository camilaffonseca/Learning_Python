# coding: utf-8

'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão. (V.3)
'''

print('- Progressão Aritmética - \n')

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

print('Os 10 primeiros termos da progressão são...')

c = 1
total = 0
quantidade_termos = 10

while quantidade_termos != 0:

    total += quantidade_termos
    
    while c <= total:
        
        print(f'| {termo}', end = ' ')
        termo += razão
        c += 1
        
    quantidade_termos = int(input('\nQuantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {total} termos mostrados')
