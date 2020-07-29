# coding: utf-8

'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

from sys import exit as sair

numero1 = float(input('Primeiro número: '))
numero2 = float(input('Segundo número: '))

menu = ('\n[1] Somar'
        '\n[2] Multiplicar'
        '\n[3] Mostrar qual é o maior'
        '\n[4] Substituir os números'
        '\n[5] Mostrar menu novamente'
        '\n[6] Sair do programa')

print(menu)

while True:
    
    operação = input('\nOperação: ')

    if operação == '1':
        resultado = numero1 + numero2
    
    elif operação == '2':
        resultado = numero1 * numero2
    
    elif operação == '3':
        if numero1 > numero2:
            resultado = numero1
        else:
            resultado = numero2
    
    elif operação == '4':
        numero1 = float(input('Primeiro número: '))
        numero2 = float(input('Segundo número: '))
    
    elif operação == '5':
        print(menu)
    
    elif operação == '6':
        sair()
    
    else:
        print(f'\nOperação inválida... \n{menu}')
    
    if operação in '1236':
        print(f'\nResultado: {resultado}')
