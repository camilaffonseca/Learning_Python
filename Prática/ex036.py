# coding: utf-8

'''
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''

numero = int(input('Digite um número inteiro: '))
base = input('''Escolha a base para conversão...
             \n[1] Binário \n[2] Octal \n[3] Hexadecimal
             \nSua opção > ''')

if base == '1':
    conversão = bin(numero)
    base = 'Binário'
elif base == '2':
    conversão = oct(numero)
    base = 'Octal'
else:
    conversão = hex(numero)
    base = 'Hexadecimal'

print(f'O número {numero} convertido para {base} fica {conversão}')
