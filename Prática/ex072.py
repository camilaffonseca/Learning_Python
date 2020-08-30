# coding: utf-8

'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas.
'''

def formatação_listas(lista):
    lista_formatada = ' | '.join(map(str, lista))
    return lista_formatada

numeros = []

while True:
    numeros.append(int(input('Número: ')))

    while True:
        opção_continuar = input('Continuar? ').upper()[0]
        if opção_continuar in 'SN':
            break
        else:
            print('Responda com SIM ou NÃO...')
    if opção_continuar == 'N':
        break

numeros_pares = []
numeros_impares = []

for item in numeros:
    if item % 2 == 0:
        numeros_pares.append(item)
    else:
        numeros_impares.append(item)

print(f'\nNúmeros pares: {formatação_listas(numeros_pares)}'
      f'\nNúmeros ímpares: {formatação_listas(numeros_impares)}'
      f'\nPrimeira lista: {formatação_listas(numeros)}')
