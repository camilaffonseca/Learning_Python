# coding: utf-8

'''
Crie um programa que declare uma matriz de dimensão 3×3
e preencha com valores lidos pelo teclado. No final,
mostre a matriz na tela, com a formatação correta
'''

matriz = [[],[],[]]

x = 0
y = 0

for y in range(0, 3):
    for x in range(0, 3):
        matriz[y].append(int(input(f'Posição [{y}, {x}]: ')))

for y in range(0, 3):
    for x in range(0, 3):
        print(f'[{matriz[y][x]:^5}]', end='')
    print()
