# coding: utf-8

'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[],[],[]]

soma_pares = soma_terceira_coluna = 0

x = y = 0

for y in range(0, 3):
    for x in range(0, 3):
        matriz[y].append(int(input(f'Posição [{y}, {x}]: ')))

        if matriz[y][x] % 2 == 0:
            soma_pares += matriz[y][x]

        if x == 2:
            soma_terceira_coluna += matriz[y][x]

for y in range(0, 3):
    for x in range(0, 3):
        print(f'[{matriz[y][x]:^5}]', end='')
    print()

matriz[1].sort()

print(f'''
A soma dos pares é {soma_pares}
A soma dos valores da terceira coluna é {soma_terceira_coluna}
O maior valor da segunda linha é {matriz[1][-1]}
''')
