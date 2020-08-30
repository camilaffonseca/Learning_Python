# coding: utf-8

'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
'''

valores = []

for c in range(1, 6):
    while True:
        try:
            valores.append(int(input(f'Valor {c}: ')))
            break
        except Exception:
            print('Digite um número inteiro...')

maior = sorted(valores)[-1]
menor = sorted(valores)[0]

posição_maior = []
posição_menor = []

for posição, ítem in enumerate(valores):
    if ítem == maior:
        posição_maior.append(posição)
    elif ítem == menor:
        posição_menor.append(posição)

print(f'\nMaior valor: {maior}  ||  Posição na lista: ',
      ' | '.join(map(str, posição_maior)),
      f'\nMenor valor: {menor}  ||  Posição na lista: ',
      ' | '.join(map(str, posição_menor)))
