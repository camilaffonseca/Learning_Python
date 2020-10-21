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
    if passo == 0:
        passo = 1

    if passo < 0:
        passo *= -1

    if início > fim:
        print(f'\n\nContagem de {início} até {fim}, com passo {passo}...\n')

        while início >= fim:
            print(
                f'| {início:^5} |',
                end='',
                flush=True
            )

            sleep(0.7)

            início -= passo

    elif início < fim:
        print(f'\n\nContagem de {início} até {fim}, com passo {passo}...\n')

        while início <= fim:
            print(
                f'| {início:^5} |',
                end='',
                flush=True
            )

            sleep(0.7)

            início += passo

    else:
        print('\nO início e o fim não podem ter o mesmo valor, '
              'senão não consigo fazer a contagem, bocó :)\n')

contador(1, 10)

contador(10, 0, 2)

print('\n\nAgora é a sua vez de personalizar a contagem :)\n')

início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(início, fim, passo)
