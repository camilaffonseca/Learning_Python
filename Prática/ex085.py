# coding: utf-8

'''
Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: início, fim e passo. Seu programa tem
que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''


from time import sleep

def contador(início, fim, passo = 1):
    if início > fim:
        while início >= fim:
            print(f'| {início:^5} |', end='', flush=True)
            sleep(0.7)
            início -= passo
    elif início < fim:
        while início <= fim:
            print(f'| {início:^5} |', end='', flush=True)
            sleep(0.7)
            início += passo
    else:
        print('O início e o fim não podem ter o mesmo valor, '
              'senão não consigo fazer a contagem, bocó :)')

print('\nContagem de 1 a 10, com passo 1...')
contador(1, 10)

print('\nContagem de 10 a 0, com passo 2...')
contador(10, 0, 2)

print('\nAgora é a sua vez de personalizar a contagem :)\n')

início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(início, fim, passo)
