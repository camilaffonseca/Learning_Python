# coding: utf-8

'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Número {c}: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'A soma dos {cont} números pares é {soma}.')
