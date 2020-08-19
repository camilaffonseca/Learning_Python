# coding: utf-8

'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

valores = []
for c in range(1, 5):
    valores.append(int(input(f'Valor {c}: ')))

valores = tuple(valores)

if 3 in valores:
    print('\nO primeiro valor 3 foi digitado na posição'
          f' {valores.index(3) + 1}')
else:
    print('\nO número 3 não foi digitado')

print(f'O número 9 apareceu {valores.count(9)} vezes')

print('\nForam digitados os números pares: ', end='')

for valor in valores:
    if valor % 2 == 0:
        print(valor, '| ', end='')
