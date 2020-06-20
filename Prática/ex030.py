# coding: utf-8

# Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar


numero = int(input('Digite um número: '))

resultado = numero % 2

if resultado == 1:
    print(f'O número {numero} é ímpar')
else:
    print(f'O número {numero} é par')
