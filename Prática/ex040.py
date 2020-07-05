# coding: utf-8

'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal 
– 3x ou mais no cartão: 20% de juros
'''

preço = float(input('Preço do produto: R$ ').replace(',', '.'))

preço_final = ''

opção = input('''
Formas de pagamento:
[1] À vista
[2] Parcelado no cartão

Sua opcão:
> ''')

if opção == '1':
    opção2 = input('\n[1] Dinheiro'
                   '\n[2] Cartão'
                   '\n\n> ')
    if opção2 == '1':
        preço_final = preço - (preço * 10 / 100)
    else:
        preço_final = preço - (preço * 5 / 100)
elif opção == '2':
    opção2 = int(input('Quantas parcelas? '))
    if opção2 > 2:
        parcelas = (preço / opção2) + ((preço / opção2) * 20 / 100)
        preço_final = parcelas * opção2
    elif opção2 == 1:
        preço_final = preço
        parcelas = preço
    else:
        preço_final = preço
        parcelas = preço / 2
    print(f'Valor parcelado em {opção2}x de R$ {parcelas:.2f} no cartão')
else:
    print('Opção inválida....')

if preço_final != '':
    print(f'Sua compra vai custar R$ {preço_final:.2f}')
