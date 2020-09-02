# coding: utf-8

'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''


pessoas = []
lista_nomes = []
maior_peso = menor_peso = 0

while True:
    pessoa = []

    while True:
        nome_pessoa = input('Nome: ').strip()

        if nome_pessoa in lista_nomes:
            print('Pessoa já cadastrada, insira outro nome.')
        else:
            break

    lista_nomes.append(nome_pessoa)
    pessoa.append(nome_pessoa)

    while True:
        try:
            pessoa.append(float(input('Peso: ')))
            break
        except Exception:
            print('Valor inválido! Tente novamente...')

    pessoas.append(pessoa)
    
    if len(pessoas) == 1:
        maior_peso = menor_peso = pessoa[1]
    else:
        if pessoa[1] > maior_peso:
            maior_peso = pessoa[1]
        elif pessoa[1] < menor_peso:
            menor_peso = pessoa[1]

    while True:
        opção_continuar = input('Continuar? ').strip().upper()[0]
        if opção_continuar in 'SN':
            break
        else:
            print('Digite SIM ou NÃO...')
    if opção_continuar == 'N':
        break

pessoas_maior_peso = []
pessoas_menor_peso = []

for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        pessoas_maior_peso.append(pessoa[0])

    if pessoa[1] == menor_peso:
        pessoas_menor_peso.append(pessoa[0])


print(len(pessoas), ' pessoas foram cadastradas',
      '\nPessoas mais leves: ', ' | '.join(map(str, pessoas_menor_peso)),
      '\nPessoas mais pesadas: ', ' | '.join(map(str, pessoas_maior_peso)))
