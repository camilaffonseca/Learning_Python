# coding: utf-8

'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''


from helpers.io import type_input


pessoas = []

while True:
    pessoa = {}

    pessoa['nome'] = type_input('name')
    pessoa['sexo'] = type_input('gender')
    pessoa['idade'] = type_input('age')

    pessoas.append(pessoa)

    opção_continuar = type_input('continue')

    if opção_continuar == 'N':
        break


soma_idades = 0

for pessoa in pessoas:
    soma_idades += pessoa['idade']

média_idades = soma_idades / len(pessoas)


mulheres = []
idade_acima_média = []

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'].title())

    if pessoa['idade'] > média_idades:
        idade_acima_média.append(pessoa['nome'].title())

if len(pessoas) > 1: 
    print(f'Foram cadastradas {len(pessoas)} pessoas\n'
          f'Média de idade: {média_idades :.2f}')
else:
    print(f'Foi cadastrada 1 pessoa')

if mulheres:
    print(
        'Mulheres: ',
        ', '.join(map(str, mulheres))
    )

if idade_acima_média:
    print(
        'Pessoas com idade acima da média: ',
        ', '.join(map(str, idade_acima_média))
    )
