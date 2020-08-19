# coding: utf-8

'''
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla. Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

lista_de_numeros = []
for loop in range(0, 5):
    lista_de_numeros.append(randint(0, 30))

numeros_aleatórios = tuple(lista_de_numeros)

print('Números gerados: ', end='')
for numero in numeros_aleatórios:
    print(f'{numero} | ', end='')

maior = menor = 0
for numero in numeros_aleatórios:
    if numeros_aleatórios.index(numero) == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

print(f'\nMaior número: {maior}'
      f'\nMenor número: {menor}')
