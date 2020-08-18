# coding: utf-8

'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag).
'''

numero = None
soma = c = 0

while numero != 0:
    try:
        numero = int(input('Número: '))

        if bool(numero) is True:
            soma += numero
            c += 1

    except Exception:
        print('Tente novamente!')

print(f'A soma dos {c} números é {soma}')
