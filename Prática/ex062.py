# coding: utf-8

'''
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um
número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    try:
        numero = int(input('Digite um número (0 a 20): '))
        if 0 <= numero <= 20:
            break
        else:
            print('Número inválido! Digite um número entre 0 e 20...')
    except Exception:
        print('Valor inválido! Tente Novamente...')

print(f'Você digitou {contagem[numero].upper()}')
