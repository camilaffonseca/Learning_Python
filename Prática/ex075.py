# coding: utf-8

'''
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e
ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

numeros = [[], []]

for c in range(1, 8):
    numero = int(input(f'Número {c}: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

numeros[0].sort()
numeros[1].sort()

print('Pares: ', ' | '.join(map(str, numeros[0])),
      '\nImpares: ', ' | '.join(map(str, numeros[1])))
