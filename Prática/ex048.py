# coding: utf-8

'''
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
'''

número = int(input('Número: '))

cont_div = 0

for c in range(1, número + 1):
    if número % c == 0:
        cont_div += 1

if cont_div == 2:
    print(f'{número} é um número primo')
else:
    print(f'{número} não é um número primo')

print(f'Foi divisível {cont_div} vezes')
