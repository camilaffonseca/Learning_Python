# coding: utf-8

'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a
condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre eles (desconsiderando o flag).
'''

número = None
soma = c = 0

while True:
    try:
        número = int(input('Número: '))
        if número == 0:
            break
        c += 1
        soma += número
        
    except Exception:
        print('Tente novamente...')

print(f'A soma dos {c} números foi {soma}')
