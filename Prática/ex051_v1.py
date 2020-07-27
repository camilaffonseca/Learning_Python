# coding: utf-8

# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0
for p in range(1, 6):
    peso = float(input(f'Peso da pessoa {p}: '))
    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        elif peso < menor_peso:
            menor_peso = peso

print(f'O menor peso foi {menor_peso} e o maior foi {maior_peso}')
