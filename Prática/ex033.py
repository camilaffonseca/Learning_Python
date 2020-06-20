# coding: utf-8

# Crie um programa que leia três números e mostre o menor e o maior deles


numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))

if numero1 < numero2 and numero1 < 3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
elif numero3 < numero1 and numero3 < numero2:
    menor = numero3

if numero1 > numero2 and numero1 > 3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
elif numero3 > numero1 and numero3 > numero2:
    maior = numero3

print(f'O maior número e o menor número são, \
respectivamente {maior} e {menor}')
