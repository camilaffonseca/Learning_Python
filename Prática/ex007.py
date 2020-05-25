# coding: utf-8

# Conversor de moeda


real = float(input('Digite uma quantidade de dinheiro em R$: '))

print(f'R${real} equivale a US${round((real * 5.68), 2)}')
