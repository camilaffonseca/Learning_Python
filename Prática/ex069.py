# coding: utf-8

'''
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
'''

valores = []

while True:
    while True:
        valor = int(input('Valor: '))

        if valor not in valores:
            valores.append(valor)
            break
        else:
            print('Número já cadastrado...')

    while True:
        opção_continuar = input('Continuar? ').upper()[0]

        if opção_continuar in 'SN':
            break
        else:
            print('Digite SIM ou NÃO...')

    if opção_continuar == 'N':
        break

valores.sort()

print('Valores digitados: ', ' | '.join(map(str, valores)))
