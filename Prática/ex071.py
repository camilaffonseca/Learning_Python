# coding: utf-8

'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []

while True:
    valores.append(int(input('Valor: ')))

    while True:
        opção_continuar = input('Continuar? ').upper()[0]
        if opção_continuar in 'SN':
            break
        else:
            print('Digite SIM ou NÃO...')

    if opção_continuar == 'N':
        break

contagem_5 = 0
posições = []

for posição, item in enumerate(valores):
    if item == 5:
        contagem_5 += 1
        posições.append(posição)

valores.sort(reverse=True)

print(f'Foram digitados {len(valores)} números\n', ' | '.join(map(str, valores)))

if 5 in valores:
    print(f'O número 5 aparece {contagem_5} vezes na lista, nas posições ', ' | '.join(map(str, posições)))
else:
    print('O número 5 não aparece na lista')
