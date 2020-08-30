# coding: utf-8

'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o
sort()). No final, mostre a lista ordenada na tela.
'''

valores = []
for c in range(1, 6):

    valor = int(input(f'Valor {c}: ')) # TODO

    if valores:
        condicao = valor > valores[-1]
    else:
        condicao = False

    if c == 1 or condicao:
        valores.append(valor)
    else:
        i = 0

        while True:
            if valor <= valores[i]:
                valores.insert(i, valor)
                break
            i += 1

print('Valores digitados: ', ' | '.join(map(str, valores)))
