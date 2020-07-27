# coding: utf-8

'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.
'''

from datetime import date

cont = 0
pessoas_maiores = []
pessoas_menores = []
for c in range(1, 8):
    nome = input(f'Nome da pessoa {c}: ')
    nascimento = int(input(f'Ano de nascimento de {nome}: '))
    idade = date.today().year - nascimento
    if idade >= 18:
        cont += 1
        pessoas_maiores.append(nome)
    else:
        pessoas_menores.append(nome)

print(f'{cont} pessoas já atingiram a maioridade:')

for pessoa in pessoas_maiores:
    print(pessoa)

print(f'{7 - cont} ainda não:')

for pessoa in pessoas_menores:
    print(pessoa)
